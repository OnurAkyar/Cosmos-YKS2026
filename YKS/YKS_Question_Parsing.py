import fitz  # PyMuPDF
import os
import re
import requests

# Ayarlar ve Yollar
pdf_path = "/content/yks-tyt-2025.pdf"
klasor_adi = "YKS_Tyt_2025_Question"

# Klasörü oluştur
os.makedirs(klasor_adi, exist_ok=True)


# 2. AŞAMA: PDF'i Parse Etme ve Kesme
try:
    doc = fitz.open(pdf_path)
    print("PDF başarıyla açıldı! Sorular parse ediliyor...")
except Exception as e:
    print(f"HATA: PDF açılamadı. Dosyayı yüklediğinden emin ol. Detay: {e}")
    exit()

# Regex: Satır başında (varsa boşlukları yoksay) sayı ve nokta yakalar
soru_regex = re.compile(r'^\s*(\d+)\.') 

print("Sorular parse ediliyor ve kesiliyor...")

for sayfa_no in range(len(doc)):
    sayfa = doc[sayfa_no]
    bloklar = sayfa.get_text("blocks")
    
    sayfa_genisligi = sayfa.rect.width
    sayfa_yuksekligi = sayfa.rect.height
    orta_cizgi = sayfa_genisligi / 2
    
    sol_sutun_sorular = []
    sag_sutun_sorular = []
    
    # Soru Başlangıçlarını ve Sütunlarını Tespit Et
    for blok in bloklar:
        x0, y0, x1, y1, metin, blok_no, blok_tipi = blok
        if blok_tipi == 0:  # Sadece metin blokları
            match = soru_regex.match(metin)
            if match:

              # KRİTİK FİLTRE: ÖSYM'nin tuzak başlıklarını atla!
                if "Bu testte" in metin or "Cevaplarınızı" in metin:
                    continue # Bu satırı es geç, soru listesine ekleme

                soru_no = match.group(1)
                # Metnin başlangıç X koordinatına bakarak sütununu belirliyoruz.
                if x0 < orta_cizgi and x0 < 100: 
                    sol_sutun_sorular.append({"no": soru_no, "y0": y0})
                elif x0 > orta_cizgi and x0 < orta_cizgi + 100: 
                    sag_sutun_sorular.append({"no": soru_no, "y0": y0})

    # Her sütunu kendi içinde yukarıdan aşağıya sırala
    sol_sutun_sorular = sorted(sol_sutun_sorular, key=lambda k: k["y0"])
    sag_sutun_sorular = sorted(sag_sutun_sorular, key=lambda k: k["y0"])
    
    # Sütunları paketle (Margin / boşluk paylarıyla beraber)
    sutunlar = [
        {"sorular": sol_sutun_sorular, "crop_x0": 25, "crop_x1": orta_cizgi - 5},
        {"sorular": sag_sutun_sorular, "crop_x0": orta_cizgi + 5, "crop_x1": sayfa_genisligi - 25}
    ]
    
    for sutun in sutunlar:
        sorular = sutun["sorular"]
        for i in range(len(sorular)):
            mevcut_soru = sorular[i]
            
            # Üstten hafif boşluk bırak
            crop_y0 = max(0, mevcut_soru["y0"] - 10) 
            
            # Sınır belirleme
            if i + 1 < len(sorular):
                crop_y1 = sorular[i+1]["y0"] - 10
            else:
                crop_y1 = sayfa_yuksekligi - 50
                
            rect = fitz.Rect(sutun["crop_x0"], crop_y0, sutun["crop_x1"], crop_y1)
            
            try:
                # VLM için cam gibi net olması adına matris büyütme
                matris = fitz.Matrix(3.0, 3.0)
                pix = sayfa.get_pixmap(matrix=matris, clip=rect)
                
                # Dosya ezilmesin diye sayfa numarası ve soru numarası formatlandı
                dosya_adi = f"sayfa_{sayfa_no+1:03d}_soru_{mevcut_soru['no'].zfill(2)}.jpg"
                kayit_yolu = os.path.join(klasor_adi, dosya_adi)
                
                pix.save(kayit_yolu)
                print(f"Başarılı: {dosya_adi}")
            except Exception as e:
                print(f"HATA: Sayfa {sayfa_no+1} Soru {mevcut_soru['no']} kesilemedi. Sebep: {e}")

print("Tüm işlemler tamamlandı! Bütünleşik soru görselleri klasörde hazır.")
