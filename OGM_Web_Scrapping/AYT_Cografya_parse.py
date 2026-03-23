import fitz  # PyMuPDF
import os
import re
import requests

# ================= 1. AYARLAR VE İNDİRME =================
#pdf_url'i kitaba göre güncelle!
pdf_url = ""
pdf_path = "cografya.pdf"
ana_klasor = "OGM_4_4_Konu_Pekistirme2"

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
    (11, 24, "AYT_Cografya", "Biyocesitlilik ve Ekosistem"),
    (25, 38, "AYT_Cografya", "Nufus Politikalari, Yerlesme Ozellikleri ve Sehirler"),
    (39, 50, "AYT_Cografya", "Uretim, Dagitim, Tuketim ve Dogal Kaynaklar"),
    (51, 62, "AYT_Cografya", "Turkiye'nin Ekonomi Politikalari ve Tarimi Etkileyen Faktorler"),
    (63, 76, "AYT_Cografya", "Turkiye'de Tarim Urunleri, Hayvancilik ve Ormancilik"),
    (77, 90, "AYT_Cografya", "Turkiye'de Madencilik, Enerji kaynaklari ve Sanayi"),
    (91, 104, "AYT_Cografya", "Turk Kulturu ve Kultur Bolgeleri"),
    (105, 118, "AYT_Cografya", "Kuresel Ticaret, Turizm ve Uluslararasi Orgutler"),
    (119, 132, "AYT_Cografya", "Cevre Sorunlari"),
    (133, 144, "AYT_Cografya", "Ekstrem Doga Olaylari ve Dogadaki Degisim"),
    (145, 158, "AYT_Cografya", "Gecmisten Gelecege Sehir ve Ekonomi"),
    (159, 172, "AYT_Cografya", "Turkiyenin Islevsel Bolgeleri ve Kalkinma Projeleri"),
    (173, 184, "AYT_Cografya", "Hizmet Sektorunun Ekonomideki Yeri"),
    (185, 198, "AYT_Cografya", "Dunyada ve Turkiye'de Ticaret"),
    (199, 212, "AYT_Cografya", "Turkiye Turizmi"),
    (213, 224, "AYT_Cografya", "Jeopolitik Konum ve Ulkelerin Gelismisligi"),
    (225, 238, "AYT_Cografya", "Enerji Nakil Hatlari ve Gunumuz Catisma Alanlari"),
    (239, 250, "AYT_Cografya", "Dogal Cevrenin Sinirliligi, Cevresel Orgut ve Anlasmalar")
]

def konu_bul(sayfa_numarasi):
    for baslangic, bitis, ders, konu in konu_haritasi:
        if baslangic <= sayfa_numarasi <= bitis:
            return ders, konu
    return None, None

# ================= 3. CEVAP ANAHTARI GİRİŞİ =================
cevap_anahtari_ham = {
   "Biyocesitlilik ve Ekosistem":"""
   1. TEST A B D D A D B D A B
2. TEST A B D B E B E D B C
3. TEST C C D E D A C B C B
4. TEST B B E D D D A A E E
    """,
    "Nufus Politikalari, Yerlesme Ozellikleri ve Sehirler":"""
    1. TEST D B E E E D B C E B B D C
2. TEST E D C E A E B B A B B D
3. TEST E B D B C B E E D
4. TEST D B E A B E A B C E
    """,
    "Uretim, Dagitim, Tuketim ve Dogal Kaynaklar":"""
    1. TEST B C C B E E D E A B E A B
2. TEST D D D C E D C C B E
3. TEST E C D C D B E B B
4. TEST D D E B C D B D C
    """,
    "Turkiye'nin Ekonomi Politikalari ve Tarimi Etkileyen Faktorler":"""
    1. TEST C E E A E E E E A C B
2. TEST B A D D A E C E D C C
3. TEST E E B C D E B A D D
4. TEST B B E A C E B B E
    """,
    "Turkiye'de Tarim Urunleri, Hayvancilik ve Ormancilik":"""
    1. TEST D B E D D B A E E B D D C
2. TEST E E C A B A D A E A C
3. TEST D E C D B A E C E
4. TEST E C C B C D D E C B A
    """,
    "Turkiye'de Madencilik, Enerji kaynaklari ve Sanayi":"""
    1. TEST D B A B E C D E B C B A
2. TEST C E D B C A B D E E
3. TEST D B E B E E D D B
4. TEST D D B E E E E C D
    """,
    "Turk Kulturu ve Kultur Bolgeleri":"""
    1. TEST D A C D D B A A C E D D
2. TEST C D A E A B E D B D B D
3. TEST D D A A D D C C A
4. TEST C A B E D E A D B E B
    """,
    "Kuresel Ticaret, Turizm ve Uluslararasi Orgutler":"""
    1. TEST D B B D D A A D B D C D D
2. TEST C B B B E C D D B
3. TEST C C C E D D E C D
4. TEST E B E A D C E D A A
    """,
    "Cevre Sorunlari":"""
    1. TEST D B E D A B A D A E E C
2. TEST B B E C D E D B D E
3. TEST A C C C E A D A
4. TEST E E A D A B C E
    """,
    "Ekstrem Doga Olaylari ve Dogadaki Degisim":"""
    1. TEST A C A D C E B D D D B B
2. TEST E C C B D B D A C E E B
3. TEST C D E E C D D C B
4. TEST A B E B B A C A E D
    """,
    "Gecmisten Gelecege Sehir ve Ekonomi":"""
    1. TEST C B D D C E C C A D E A
2. TEST C D E A D A B A E B D A
3. TEST D A E C B D E E D D A B
4. TEST D E E D C B C A B C B E
    """,
    "Turkiyenin Islevsel Bolgeleri ve Kalkinma Projeleri":"""
    1. TEST C D B E B E B A C A D B
2. TEST E A C A C D C C D D B
3. TEST D D A D C C D D B B
4. TEST C D A A D B C B E C E
    """,
    "Hizmet Sektorunun Ekonomideki Yeri":"""
    1. TEST B E C D A D C B C C C B
2. TEST B A A A B C C A C C C
3. TEST C B D D A E C C D C D
4. TEST C D D E D B C E C C D
    """,
    "Dunyada ve Turkiye'de Ticaret":"""
    1. TEST E D C E D D B C E E
2. TEST C B B A B D C D B
3. TEST B A B A E A E E A
4. TEST C A E D C B C A B B
    """,
    "Turkiye Turizmi":"""
    1. TEST D A C A E E B A B E E A
2. TEST B D C E B A A D E C
3. TEST D E D E E D D A A D E
4. TEST A D E E A E B A A D E B
    """,
    "Jeopolitik Konum ve Ulkelerin Gelismisligi":"""
    1. TEST B C E A D A E B C C D
2. TEST A C C B D A A B E E A
3. TEST B C C A B E E E C A C D
4. TEST E B D D D B A D C D E A
    """,
    "Enerji Nakil Hatlari ve Gunumuz Catisma Alanlari":"""
    1. TEST B C C B B D D E A D A C C A
2. TEST C D C B E B D D B C B
3. TEST C B B C D D E D A C B
4. TEST E C B A D C B E A C
    """,
    "Dogal Cevrenin Sinirliligi, Cevresel Orgut ve Anlasmalar":"""
    1. TEST C A E B D E D E B C C C
2. TEST B D B C B B C B D E D
3. TEST D D E D B C E B D E C
4. TEST A A E B B A C C E C
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
kaydedilen_sorular = set()

#Kitabın içerisinde sorular olan son sayfasını belirtir. Kitaba göre güncelle!
son_soru_sayfasi = 250

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

                # 1. Önce kendi sütununda altına bak (Standart Durum)
                for j in range(i + 1, len(ogeler)):
                    siradaki_oge = ogeler[j]

                    if siradaki_oge["tip"] == "soru":
                        break

                    if siradaki_oge["tip"] in ["cozum", "cevap_satiri"]:
                        cozumlu_mu = True
                        if siradaki_oge.get("bulunan_cevap", "Bulunamadi") != "Bulunamadi":
                            bulunan_cevap = siradaki_oge["bulunan_cevap"]

                # 2. EĞER KENDİ SÜTUNUNDA YOKSA YAN SÜTUNA (SAĞA VEYA SOLA) BAK
                sayfada_cozum_var = any(o["tip"] in ["cozum", "cevap_satiri"] for o in sol_sutun_ogeler + sag_sutun_ogeler)
                if not cozumlu_mu and sayfada_cozum_var:
                    diger_sutun = sag_sutun_ogeler if sutun["crop_x0"] < orta_cizgi else sol_sutun_ogeler
                    for diger_oge in diger_sutun:
                        if diger_oge["y0"] > mevcut_oge["y0"] - 50:
                            
                            # Yan sütunda aşağı doğru okurken başka bir "Soru"ya çarparsak dur!
                            if diger_oge["tip"] == "soru":
                                break
                                
                            # Eğer Çözüm veya Cevap satırına denk gelirsek kaydet ve okumaya DEVAM ET
                            if diger_oge["tip"] in ["cozum", "cevap_satiri"]:
                                cozumlu_mu = True
                                if diger_oge.get("bulunan_cevap", "Bulunamadi") != "Bulunamadi":
                                    bulunan_cevap = diger_oge["bulunan_cevap"]


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
                    dosya_adi = f"question-{aktif_ders}_{soru_no_int}. answer-{dogru_cevap}.jpg"
                    kayit_yolu = os.path.join(hedef_klasor, dosya_adi)


                    # === ÇAKIŞMA KONTROLÜ (OVERWRİTE/SADECE SAYIYA GÖRE) ===
                    soru_kimligi = f"{aktif_konu}/{aktif_alt_klasor}/Soru_{soru_no_int}"
                    if soru_kimligi in kaydedilen_sorular:
                        hata_listesi.append(f"⚠️  Çakışma Hatası: {aktif_konu}/{aktif_alt_klasor} testindeki {soru_no_int}. soru birden fazla kez kesildi!")
                    else:
                        kaydedilen_sorular.add(soru_kimligi)

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
