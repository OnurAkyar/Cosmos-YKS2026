import asyncio
import requests
import torch
from playwright.async_api import async_playwright
from transformers import pipeline

device = "cuda:0" if torch.cuda.is_available() else "cpu"
print(f"Whisper modeli yükleniyor... (Kullanılan donanım: {device})")

# 1. GÜNCELLEME: En iyi model olan "large-v3-turbo" seçildi.
# 2. GÜNCELLEME: stride_length_s eklendi (Sesler kesilirken kelime kaybı olmasın diye kesişim payı bırakır)
transcriber = pipeline(
    "automatic-speech-recognition", 
    model="openai/whisper-large-v3-turbo", 
    device=device,
    chunk_length_s=30,
    stride_length_s=[4, 2] # 30 saniyenin son 4 saniyesi ile yeni parçanın ilk 2 saniyesini üst üste bindirir.
)

async def metne_cevir(test_url, test_soru_sayisi=3):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        guncel_video_linki = None

        async def intercept_request(request):
            nonlocal guncel_video_linki
            if ".mp4" in request.url:
                guncel_video_linki = request.url

        page.on("request", intercept_request)

        print("Sayfaya gidiliyor...")
        await page.goto(test_url, wait_until="networkidle")
        await page.wait_for_selector("button:has-text('Çözümü İzle')", timeout=15000)
        buttons = page.locator("button:has-text('Çözümü İzle')")
        
        count = await buttons.count()
        islem_sayisi = min(count, test_soru_sayisi)
        
        for i in range(islem_sayisi):
            print(f"\n--- Soru {i+1} İşleniyor ---")
            guncel_video_linki = None 
            
            await buttons.nth(i).click()
            
            for _ in range(10):
                if guncel_video_linki:
                    break
                await asyncio.sleep(0.5)
                
            if guncel_video_linki:
                print(f"Video bulundu: {guncel_video_linki}")
                video_adi = f"soru_{i+1}.mp4"
                
                print("Video indiriliyor...")
                cevap = requests.get(guncel_video_linki)
                with open(video_adi, 'wb') as f:
                    f.write(cevap.content)
                
                print("Whisper metne çeviriyor (Bu biraz daha uzun sürebilir ama kusursuz olacak)...")
                
                # 3. GÜNCELLEME: batch_size=8 eklenerek GPU'nun sesi çok daha hızlı işlemesi sağlandı
                sonuc = transcriber(
                    video_adi, 
                    generate_kwargs={"language": "turkish", "task": "transcribe"},
                    batch_size=8 
                )
                cozum_metni = sonuc["text"].strip()
                print(f"Çeviri Tamamlandı:\n{cozum_metni}\n") 
                
            else:
                print("Bu soru için video linki yakalanamadı.")

            await page.keyboard.press("Escape")
            await asyncio.sleep(1)

        await browser.close()
        print("\nİşlem bitti!")

test_linki = "https://mebi.eba.gov.tr/student/exam/diagnostic/qr-details/c04a74a1-1485-4edb-85e8-08ddd54c9252"
await metne_cevir(test_linki, test_soru_sayisi=3)
