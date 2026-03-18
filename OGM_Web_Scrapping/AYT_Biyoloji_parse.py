import fitz  # PyMuPDF
import os
import re
import requests

# ================= 1. AYARLAR VE İNDİRME =================
#pdf_url'i kitaba göre güncelle!
pdf_url = "https://ogm-large-cdn.eba.gov.tr/ogm-materyal/konu-pekistirme/ayt/biyoloji/biyoloji.pdf"
pdf_path = "ayt-biyoloji-konu-pekistirme.pdf"
ana_klasor = "OGM_4_4_Konu_Pekistirme"

os.makedirs(ana_klasor, exist_ok=True)
fitz.TOOLS.mupdf_display_errors(False)

if not os.path.exists(pdf_path):
    print("PDF internetten indiriliyor, lütfen bekle...")
    response = requests.get(pdf_url)
    if response.status_code == 200:
        with open(pdf_path, "wb") as f:
            f.write(response.content)
        print("PDF başarıyla indirildi!")
else:
    print("PDF zaten bilgisayarda var, indirme aşaması atlanıyor...")

#jpg formatını isimlendirmek için eklendi! Kitaba göre güncelle!
# ================= 2. KONU HARİTASI =================
konu_haritasi = [
    (11, 24, "AYT_Biyoloji", "Sinir Sistemi"),
    (25, 34, "AYT_Biyoloji", "Endokrin Sistem"),
    (35, 44, "AYT_Biyoloji", "Duyu Organlari"),
    (45, 58, "AYT_Biyoloji", "Destek ve Hareket Sistemi"),
    (59, 76, "AYT_Biyoloji", "Sindirim Sistemi"),
    (77, 94, "AYT_Biyoloji", "Dolasim Sistemleri"),
    (95, 104, "AYT_Biyoloji", "Bagisiklik Cesitleri ve Savunma Mekanizmalari"),
    (105, 118, "AYT_Biyoloji", "Solunum Sistemi"),
    (119, 132, "AYT_Biyoloji", "Uriner Sistem"),
    (133, 148, "AYT_Biyoloji", "Ureme Sistemi ve Embriyonik Gelisim"),
    (149, 160, "AYT_Biyoloji", "Komunite Ekolojisi"),
    (161, 170, "AYT_Biyoloji", "Populasyon Ekolojisi"),
    (171, 184, "AYT_Biyoloji", "Nukleik Asitlerin Kesfi ve Onemi"),
    (185, 196, "AYT_Biyoloji", "Genetik Sifre ve Protein Sentezi"),
    (197, 208, "AYT_Biyoloji", "Genetik Muhendisligi ve Biyoteknoloji"),
    (209, 222, "AYT_Biyoloji", "Canlilik ve Enerji - Fotosentez - Kemosentez"),
    (223, 238, "AYT_Biyoloji", "Hucresel Solunum - Fermantasyon - Fotosentez ve Solunum Iliskisi"),
    (239, 250, "AYT_Biyoloji", "Bitkilerin Yapisi"),
    (251, 262, "AYT_Biyoloji", "Bitkilerde Madde Tasinmasi"),
    (263, 274, "AYT_Biyoloji", "Bitkilerde Eseyli Ureme"),
    (275, 284, "AYT_Biyoloji", "Canlilar ve Cevre")
]

def konu_bul(sayfa_numarasi):
    for baslangic, bitis, ders, konu in konu_haritasi:
        if baslangic <= sayfa_numarasi <= bitis:
            return ders, konu
    return None, None

# ================= 3. CEVAP ANAHTARI GİRİŞİ =================
cevap_anahtari_ham = {
   "Sinir Sistemi":"""
   1. TEST E D C C E A A B C E D
2. TEST E C D B A D B D B C C
3. TEST E C D C E D B C D C D C
4. TEST C C D D E A D D C B
    """,
    "Endokrin Sistem":"""
    1. TEST B D C B E D D E A C B A
2. TEST B C A D D A E B C E
3. TEST D D E D B C A D C
4. TEST B C E A D D C B B E
    """,
    "Duyu Organlari":"""
    1. TEST D B B D A B A E B A B
2. TEST D E C D D A C A D D C D
3. TEST D A C A C A B D B D
4. TEST D C B E D E D C B
    """,
    "Destek ve Hareket Sistemi":"""
    1. TEST C E A D C E D B B C C C
2. TEST D D A D D C D E E D D E
3. TEST B E E E C B E A E E D
4. TEST B A B C D C A A B B E
    """,
    "Sindirim Sistemi":"""
    1. TEST B C D E E B A E A E E
2. TEST - A A B D A E E B B
2. TEST - B D E A D E C C A
3. TEST A C D E E E D C E D
4. TEST B A A A D E E E
    """,
    "Dolasim Sistemleri":"""
    1. TEST - A B D E C A C B B E D C
1. TEST - B D B B D C C E B D C D
2. TEST C E B D E A D D C E
3. TEST E A A E D C B C A E
4. TEST C E C D B E A E
    """,
    "Bagisiklik Cesitleri ve Savunma Mekanizmalari":"""
    1. TEST D C B E D B D C D B B D
2. TEST B E A C D B A D A E C
3. TEST D B A B C A E D C B B E
4. TEST A E D C C A E C E
    """,
    "Solunum Sistemi":"""
    1. TEST B E E C B D D A A D
2. TEST D E B B C B B B D A
3. TEST E B E C C E C B D D
4. TEST E D A E E C
    """,
    "Uriner Sistem":"""
    1. TEST E C D E A E B D E D D B D C B E
2. TEST C D D C D A D B B A C B
3. TEST D C B A A C D C B
4. TEST D D B C C B C C
    """,
    "Ureme Sistemi ve Embriyonik Gelisim":"""
    1. TEST D C E A E D C E E A D E C
2. TEST - A B A B B A B B D C
2. TEST - B B C B C E D D
3. TEST E D D D C C D D E B C
4. TEST D A E B C C
    """,
    "Komunite Ekolojisi":"""
    1. TEST E A D C E D D C A B A
2. TEST D C E E D D C A C E A
3. TEST C D E E A E D D C D
4. TEST C C C B E A A B
    """,
    "Populasyon Ekolojisi":"""
    1. TEST D B D D C E D C B C E
2. TEST C D C C E B E E C C C
3. TEST C E C D E E C E D C C D
4. TEST E C A B A E C C
    """,
    "Nukleik Asitlerin Kesfi ve Onemi":"""
    1. TEST E C C E C C D D B C D C
2. TEST C B E D C D B D D B A
3. TEST D C A E B E A D E A E C
4. TEST A D C E B B D E
    """,
    "Genetik Sifre ve Protein Sentezi":"""
    1. TEST B D E C C E C C B C A C
2. TEST C B D B B D E C D A B
3. TEST E A C A D B A D B E A
4. TEST B C D C A A C A C D
    """,
    "Genetik Muhendisligi ve Biyoteknoloji":"""
    1. TEST D E C E E E A D B D D C
2. TEST D E C C A C B A C B
3. TEST A D E C B E B D B B
4. TEST C B D E E A E D
    """,
    "Canlilik ve Enerji - Fotosentez - Kemosentez":"""
    1. TEST D E C D C A A D B B D E E
2. TEST E C C A D D D C C A B E
3. TEST C D D C C C D A D C B C D E
4. TEST C D B A B E A D
    """,
    "Hucresel Solunum - Fermantasyon - Fotosentez ve Solunum Iliskisi":"""
    1. TEST A A E B B E D C B D D
2. TEST - A B C E D A E D D D C B
2. TEST - B A D D B D D C B A A
3. TEST A D A C C D A C B E D D
4. TEST B D A E C D D D
    """,
    "Bitkilerin Yapisi":"""
    1. TEST E A E C D E D D E C E C
2. TEST C A D E A B B A D E B E
3. TEST D D D C B D E E D E A
4. TEST C E D C D D C B C B B C
    """,
    "Bitkilerde Madde Tasinmasi":"""
    1. TEST C E B D E A D E E E B A
2. TEST C E C D E E B D A E C E
3. TEST D C D D A B E C B E
4. TEST B C C C E B D E C
    """,
    "Bitkilerde Eseyli Ureme":"""
    1. TEST A A D B A B E A A E D A
2. TEST D E D D D A E B A B C D
3. TEST D C E B D B E D B D C B
4. TEST A C D B C E D D E A E D
    """,
    "Canlilar ve Cevre":"""
    1. TEST D C C E A E C B D D E
2. TEST B E C A D D A E
3. TEST D A B A E B A
4. TEST E C D C B D B C
    """,
}

manuel_cevap_anahtari = {}
for konu, metin in cevap_anahtari_ham.items():
    manuel_cevap_anahtari[konu] = {}
    test_sayaci = 1
    for satir in metin.strip().splitlines():
        satir = satir.strip()
        if not satir:
            continue
        match = re.match(r'\d+\.\s*TEST(?:\s*[-–]\s*[A-Z])?\s+(.*)', satir)
        if match:
            harfler = match.group(1).replace(" ", "").strip()
            manuel_cevap_anahtari[konu][f"Test_{test_sayaci}"] = harfler
            test_sayaci += 1

# ====================================================================
# ====================================================================

try:
    doc = fitz.open(pdf_path)
    print("PDF başarıyla açıldı! Çözümler ayıklanıyor...")
except Exception as e:
    print(f"HATA: PDF açılamadı. Detay: {e}")
    exit()

soru_regex = re.compile(r'(?:^|\n)\s*(\d+)\.', re.MULTILINE)
cozum_regex = re.compile(r'(?:^|\n)\s*Ç[öoOÖ]z[üuUÜ]m[ü]?\s*(:|\n|$)', re.IGNORECASE | re.MULTILINE)
cozum_cevabi_regex = re.compile(r'Cevap\s*[:\.]?\s*([A-E])\b', re.IGNORECASE)

konu_son_soru = {}
konu_test_sayaci_harita = {}
konu_test_durumu = {}

# === HATA YAKALAMA VE RAPORLAMA DEĞİŞKENLERİ ===
basarili_kesim = 0
hata_listesi = []
test_istatistik = {} 

#Kitabın içerisinde sorular olan son sayfasını belirtir. Kitaba göre güncelle!
son_soru_sayfasi = 284

for sayfa_no in range(len(doc)):
    if sayfa_no >= son_soru_sayfasi:
        break

    gercek_sayfa_no = sayfa_no + 1

    aktif_ders, aktif_konu = konu_bul(gercek_sayfa_no)
    if aktif_ders is None:
        continue

    sayfa = doc[sayfa_no]

    bloklar_dict = sayfa.get_text("dict")["blocks"]

    sayfa_genisligi = sayfa.rect.width
    sayfa_yuksekligi = sayfa.rect.height
    orta_cizgi = sayfa_genisligi / 2

    sol_sutun_ogeler = []
    sag_sutun_ogeler = []

    for blok in bloklar_dict:
        x0, y0, x1, y1 = blok.get("bbox", (0, 0, 0, 0))
        blok_tipi = blok.get("type", -1)

        if blok_tipi == 0:
            tam_metin = ""
            ilk_span_font = ""
            ilk_span_flags = 0
            span_bulundu = False
            test_kelimesi_bold_mu = False

            for satir in blok.get("lines", []):
                satir_metni = ""
                for span in satir.get("spans", []):
                    span_text = span.get("text", "")
                    
                    if "test" in span_text.lower():
                        span_font = span.get("font", "").lower()
                        span_flags = span.get("flags", 0)
                        if ("bold" in span_font) or (span_flags & 16):
                            test_kelimesi_bold_mu = True

                    satir_metni += span_text

                    if not span_bulundu and span_text.strip():
                        ilk_span_font = span.get("font", "").lower()
                        ilk_span_flags = span.get("flags", 0)
                        span_bulundu = True
                
                tam_metin += satir_metni + "\n"

            match_soru = soru_regex.search(tam_metin)
            match_cozum = cozum_regex.search(tam_metin)
            cevap_yakala = cozum_cevabi_regex.search(tam_metin)

            gercek_soru_mu = False

            if match_soru:
                bold_mu = ("bold" in ilk_span_font) or (ilk_span_flags & 16)

                test_basligi_sablonu = re.search(r'\s*\d+\.\s*TEST', tam_metin)
                gercekten_test_basligi_mi = test_basligi_sablonu and test_kelimesi_bold_mu

                if bold_mu and not gercekten_test_basligi_mi:
                    sutun_sol_marjinda_mi = (x0 < 60) or (orta_cizgi - 5 < x0 < orta_cizgi + 60)
                    if sutun_sol_marjinda_mi:
                        gercek_soru_mu = True

            if gercek_soru_mu or match_cozum or cevap_yakala:
                oge = {"y0": y0, "y1": y1}

                if gercek_soru_mu:
                    oge["tip"] = "soru"
                    oge["no"] = int(match_soru.group(1))
                elif match_cozum:
                    oge["tip"] = "cozum"
                    if cevap_yakala:
                        oge["bulunan_cevap"] = cevap_yakala.group(1).upper()
                elif cevap_yakala:
                    oge["tip"] = "cevap_satiri"
                    oge["bulunan_cevap"] = cevap_yakala.group(1).upper()

                if x0 < orta_cizgi:
                    sol_sutun_ogeler.append(oge)
                else:
                    sag_sutun_ogeler.append(oge)

    sol_sutun_ogeler = sorted(sol_sutun_ogeler, key=lambda k: k["y0"])
    sag_sutun_ogeler = sorted(sag_sutun_ogeler, key=lambda k: k["y0"])

    sutunlar = [
        {"ogeler": sol_sutun_ogeler, "crop_x0": 25, "crop_x1": orta_cizgi - 5},
        {"ogeler": sag_sutun_ogeler, "crop_x0": orta_cizgi + 5, "crop_x1": sayfa_genisligi - 25}
    ]

    for sutun in sutunlar:
        ogeler = sutun["ogeler"]
        for i in range(len(ogeler)):
            mevcut_oge = ogeler[i]

            if mevcut_oge["tip"] == "soru":
                soru_no_int = mevcut_oge["no"]

                cozumlu_mu = False
                bulunan_cevap = "Bulunamadi"

                for j in range(i + 1, len(ogeler)):
                    siradaki_oge = ogeler[j]

                    if siradaki_oge["tip"] == "soru":
                        break

                    if siradaki_oge["tip"] == "cozum":
                        cozumlu_mu = True
                        if siradaki_oge.get("bulunan_cevap", "Bulunamadi") != "Bulunamadi":
                            bulunan_cevap = siradaki_oge["bulunan_cevap"]

                    elif siradaki_oge["tip"] == "cevap_satiri":
                        if cozumlu_mu:
                            bulunan_cevap = siradaki_oge["bulunan_cevap"]

                if aktif_konu not in konu_son_soru:
                    konu_son_soru[aktif_konu] = 0
                    konu_test_sayaci_harita[aktif_konu] = 0
                    konu_test_durumu[aktif_konu] = "Cozumlu_Sorular"

                if soru_no_int == 1:
                    if konu_son_soru[aktif_konu] == 0:
                        if cozumlu_mu:
                            konu_test_durumu[aktif_konu] = "Cozumlu_Sorular"
                        else:
                            konu_test_sayaci_harita[aktif_konu] = 1
                            konu_test_durumu[aktif_konu] = "Test_1"
                    elif konu_son_soru[aktif_konu] > 1:
                        konu_test_sayaci_harita[aktif_konu] += 1
                        test_no = konu_test_sayaci_harita[aktif_konu]
                        konu_test_durumu[aktif_konu] = f"Test_{test_no}"

                konu_son_soru[aktif_konu] = soru_no_int
                aktif_alt_klasor = konu_test_durumu[aktif_konu]

                dogru_cevap = "Bulunamadi"
                if cozumlu_mu:
                    dogru_cevap = bulunan_cevap
                else:
                    if aktif_konu in manuel_cevap_anahtari and aktif_alt_klasor in manuel_cevap_anahtari[aktif_konu]:
                        cevap_listesi = manuel_cevap_anahtari[aktif_konu][aktif_alt_klasor]
                        indeks = soru_no_int - 1

                        # === HATA YAKALAMA (INDEX ERROR) ===
                        if 0 <= indeks < len(cevap_listesi):
                            dogru_cevap = cevap_listesi[indeks]
                        else:
                            dogru_cevap = "X"
                            hata_listesi.append(f"⚠️  {aktif_konu}/{aktif_alt_klasor} → Soru {soru_no_int} için cevap yok (anahtarda {len(cevap_listesi)} cevap var)")
                    else:
                        dogru_cevap = "X"
                        if aktif_alt_klasor != "Cozumlu_Sorular":
                            hata_listesi.append(f"⚠️  Bilinmeyen bölüm veya cevap anahtarı yok: {aktif_konu}/{aktif_alt_klasor}, soru {soru_no_int}")

                crop_y0 = max(0, mevcut_oge["y0"] - 5)

                if i + 1 < len(ogeler):
                    crop_y1 = ogeler[i+1]["y0"] - 5
                else:
                    crop_y1 = sayfa_yuksekligi - 25

                rect = fitz.Rect(sutun["crop_x0"], crop_y0, sutun["crop_x1"], crop_y1)

                try:
                    matris = fitz.Matrix(3.0, 3.0)
                    pix = sayfa.get_pixmap(matrix=matris, clip=rect)

                    hedef_klasor = os.path.join(ana_klasor, aktif_ders, aktif_konu, aktif_alt_klasor)
                    os.makedirs(hedef_klasor, exist_ok=True)

                    #Kitaba göre ve isteğe göre jpg isimlendirme kısmını güncelle!
                    dosya_adi = f"question-Ayt_Biyoloji_{soru_no_int}. answer-{dogru_cevap}.jpg"
                    kayit_yolu = os.path.join(hedef_klasor, dosya_adi)

                    # === ÇAKIŞMA (OVERWRITE) KONTROLÜ ===
                    if os.path.exists(kayit_yolu):
                        hata_listesi.append(f"⚠️  Çakışma: {aktif_konu}/{aktif_alt_klasor}/{dosya_adi} zaten var, üzerine yazılıyor.")

                    pix.save(kayit_yolu)
                    
                    # === BAŞARILI KESİM VE İSTATİSTİK TAKİBİ ===
                    basarili_kesim += 1
                    istatistik_anahtari = f"{aktif_konu} - {aktif_alt_klasor}"
                    test_istatistik[istatistik_anahtari] = test_istatistik.get(istatistik_anahtari, 0) + 1

                except Exception as e:
                    hata_listesi.append(f"❌ Kayıt hatası: {aktif_konu}/{aktif_alt_klasor}/{dosya_adi} → {e}")

# ================= 8. RAPOR EKRANI =================
print("\n" + "=" * 60)
print("  📈 SONUÇ RAPORU")
print("=" * 60)
print(f"  ✅ Başarılı kesim   : {basarili_kesim}")
print(f"  ❌ Hata/Uyarı sayısı: {len(hata_listesi)}")
print("\n  📁 Klasör bazlı dağılım:")

for klasor_adi, sayi in test_istatistik.items():
    konu, alt_klasor = klasor_adi.rsplit(" - ",1)
    beklenen = "?"
    
    if konu in manuel_cevap_anahtari and alt_klasor in manuel_cevap_anahtari[konu]:
        beklenen = len(manuel_cevap_anahtari[konu][alt_klasor])
        
    eslesme = "✓" if str(sayi) == str(beklenen) else "✗"
    print(f"     {eslesme} {klasor_adi}: {sayi} soru  (beklenen: {beklenen})")

if hata_listesi:
    print("\n  ⚠️  Uyarılar / Hatalar:")
    for h in hata_listesi:
        print(f"     {h}")

print("=" * 60)
print("  🎉 İşlem tamamlandı!")
print("=" * 60)
