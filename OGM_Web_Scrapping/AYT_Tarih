import fitz  # PyMuPDF
import os
import re
import requests

# ================= 1. AYARLAR VE İNDİRME =================
#pdf_url'i kitaba göre güncelle!
pdf_url = "https://ogm-large-cdn.eba.gov.tr/ogm-materyal/konu-pekistirme/ayt/tarih/tarih.pdf"
pdf_path = "tarih.pdf"
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
    (11, 20, "Tarih", "Tarih ve Zaman"),
    (21, 30, "Tarih", "Insanligin Ilk Donemleri"),
    (31, 42, "Tarih", "Orta Cag'da Dunya"),
    (43, 54, "Tarih", "Ilk ve Orta Caglarda Turk Dunyasi"),
    (55, 66, "Tarih", "Islam Medeniyetinin Dogusu"),
    (67, 80, "Tarih", "Turklerin Islamiyet'i Kabulu ve Ilk Turk Islam Devletleri"),
    (81, 92, "Tarih", "Yerlesme ve Devletlesme Surecinde Selcuklu Turkiyesi"),
    (93, 104, "Tarih", "Beylikten Devlete Osmanli Siyaseti (1302-1453)"),
    (105, 116, "Tarih", "Devletlesme Surecinde Savascilar ve Askerler"),
    (117, 128, "Tarih", "Beylikten Devlete Osmanli Medeniyeti"),
    (129, 142, "Tarih", "Dunya Gucu Osmanli (1453-1595)"),
    (143, 154, "Tarih", "Sultan ve Osmanli Merkez Teskilati"),
    (155, 166, "Tarih", "Klasik Cagda Osmanli Toplum Duzeni"),
    (167, 176, "Tarih", "Degisen Dunya Dengeleri Karsisinda Osmanli Siyaseti (1595-1774)"),
    (177, 186, "Tarih", "Degisim Caginda Avrupa ve Osmanli"),
    (187, 198, "Tarih", "Devrimler Caginda Degisen Devlet - Toplum Iliskileri"),
    (199, 212, "Tarih", "Uluslararasi Iliskilerde Denge Stratejisi (1774-1914)"),
    (213, 226, "Tarih", "XIX. ve XX. Yuzyilda Degisen Sosyo-Ekonomik Hayat"),
    (227, 236, "Tarih", "20. Yuzyil Baslarinda Osmanli Devleti ve Dunya"),
    (237, 246, "Tarih", "Milli Mucadele"),
    (247, 258, "Tarih", "Ataturkculuk ve Turk Inkilabi"),
    (259, 268, "Tarih", "Iki Savas Arasindaki Donemde Turkiye ve Dunya"),
    (269, 278, "Tarih", "II. Dunya Savasi Surecinde Turkiye ve Dunya"),
    (279, 288, "Tarih", "II. Dunya Savasi Sonrasinda Turkiye ve Dunya"),
    (289, 298, "Tarih", "Toplumsal Devrim Caginda Dunya ve Turkiye"),
    (299, 308, "Tarih", "21. Yuzyilin Esiginde Turkiye ve Dunya")
]
def konu_bul(sayfa_numarasi):
    for baslangic, bitis, ders, konu in konu_haritasi:
        if baslangic <= sayfa_numarasi <= bitis:
            return ders, konu
    return None, None

# ================= 3. CEVAP ANAHTARI GİRİŞİ =================
cevap_anahtari_ham = {
   "Tarih ve Zaman":"""
   1. TEST B B D C C D B D C D D A
2. TEST A A D C D E A D D B C A
3. TEST E D E A C A B E E B E A
4. TEST A A D E B D B C B C A B B
    """,
    "Insanligin Ilk Donemleri":"""
    1. TEST A A C D B A D A E B B E E
2. TEST C C B E C E D C B A E E D C D
3. TEST C C E A E D C E B D E A B D E A
4. TEST A E A B A B D A A E D C E B
    """,
    "Orta Cag'da Dunya":"""
    1. TEST D A B E A C D A B C E D
2. TEST A C D D C C A E E E C B
3. TEST D B A D B E A E C E C B
4. TEST A E D A C E E C D C A C D
    """,
    "Ilk ve Orta Caglarda Turk Dunyasi":"""
    1. TEST D E D D D E D C D C E E C
2. TEST E E E D B E C B A D C C E C A
3. TEST D A D C C C D A C A E C D A C A
4. TEST B E A A D E A C C D C E D B C E E D D
    """,
    "Islam Medeniyetinin Dogusu":"""
    1. TEST A A B D C A B C A E A E E A B
2. TEST E B C D B D D C B B B E B D C D D
3. TEST D D C E A D E E D B B E E C A C A A
4. TEST D E D A C A E D C C D C A A D D
    """,
    "Turklerin Islamiyet'i Kabulu ve Ilk Turk Islam Devletleri":"""
    1. TEST D E D A D C A A E B C E C C E A
2. TEST C D C E A C D A B B D B C E E
3. TEST C E B E C E E A B D C A B C B E
4. TEST E C B D E B A A C C B D B B B E B
    """,
    "Yerlesme ve Devletlesme Surecinde Selcuklu Turkiyesi":"""
    1. TEST B E E D B E E D C C C D B
2. TEST B A D C C B C D E A A B A
3. TEST D C A B D B C A A D A E A
4. TEST D E A B A E B B D B C E D C E
    """,
    "Beylikten Devlete Osmanli Siyaseti (1302-1453)":"""
    1. TEST A E D B D E A D D C E B
2. TEST C E E D D A D D E C D
3. TEST D C E B C E E D A E B A
4. TEST D C B A A E D A C E B B D
    """,
    "Devletlesme Surecinde Savascilar ve Askerler":"""
    1. TEST D D E D A B D B C A B
2. TEST D A C B E B A A E E C D
3. TEST D A A B C C E E E D
4. TEST D E B C D C D A B E C D
    """,
    "Beylikten Devlete Osmanli Medeniyeti":"""
    1. TEST E A B D C B B D E B B A
2. TEST E A B A E B A D D E C A C
3. TEST E D A D C A D B E C C B E
4. TEST E A B D E C C A D C D E
    """,
    "Dunya Gucu Osmanli (1453-1595)":"""
    1. TEST A A E E D C A B C C A C B
2. TEST C A C C D C C C D E D D B
3. TEST D E E B E A B D B D C A
4. TEST B A B D B A E B E D A B B
    """,
    "Sultan ve Osmanli Merkez Teskilati":"""
    1. TEST A C E D E B B A E C C D
2. TEST E D C D C E D D A E D A
3. TEST D D C C B D B B E D C D
4. TEST C A B D C D E B B E C A
    """,
    "Klasik Cagda Osmanli Toplum Duzeni":"""
    1. TEST E E E C A A D E C B A E E
2. TEST C B E B E B B E A C C B A
3. TEST E B A A B C A C E D B A A
4. TEST D E D C A B C E D A E B A
    """,
    "Degisen Dunya Dengeleri Karsisinda Osmanli Siyaseti (1595-1774)":"""
    1. TEST A D A D E E C C D D C D D
2. TEST E E B C D B D D D C D E
3. TEST C E B C E A A A D A C D
4. TEST A C C D A D C D A D B C B
    """,
    "Degisim Caginda Avrupa ve Osmanli":"""
    1. TEST E B A D D D E D E E C
2. TEST C E E E B B A C E E D A
3. TEST C E A C E C C E D
4. TEST E C C A E C D D A B B B
    """,
    "Devrimler Caginda Degisen Devlet - Toplum Iliskileri":"""
    1. TEST C D D B D E C E A E D
2. TEST C D D C E B C C C E A
3. TEST B E D E D D A A E E D D
4. TEST E B C E E E A A B B A A
    """,
    "Uluslararasi Iliskilerde Denge Stratejisi (1774-1914)":"""
    1. TEST B C B E C D C B D D D A B A A B
2. TEST A C C D B C D E C C C E E B
3. TEST B C C E E A A A D C E C D E
4. TEST D E D D D C E C B A A B D
    """,
    "XIX. ve XX. Yuzyilda Degisen Sosyo-Ekonomik Hayat":"""
    1. TEST E E B C C C E E E B E
2. TEST A C D C D D C E B E C E C
3. TEST B E A E E E D E E E C
4. TEST E B B A A A B B E A A E B
    """,
    "20. Yuzyil Baslarinda Osmanli Devleti ve Dunya":"""
    1. TEST D C A E A B A B D E C B
2. TEST B A C A B A C A B C C B
3. TEST C B E A C B A B A D D B
4. TEST B E E A A E D A A B C D
    """,
    "Milli Mucadele":"""
    1. TEST B E D E B C C A A D C E
2. TEST B C A D B C D E A C C E
3. TEST E B C C E A D E A B C C
4. TEST A C C E A B B D E E C A
    """,
    "Ataturkculuk ve Turk Inkilabi":"""
    1. TEST C B D E C C C B D D A E
2. TEST A B E B E E A C A B E D
3. TEST A C D D C E D D C B C E
4. TEST A C B D C E C D B C D E
    """,
    "Iki Savas Arasindaki Donemde Turkiye ve Dunya":"""
    1. TEST B E A D E A B C D A C C
2. TEST D B D B C D E C E A B C
3. TEST C C B D D B E B C B D E
4. TEST A E D B D C B E C A B D
    """,
    "II. Dunya Savasi Surecinde Turkiye ve Dunya":"""
    1. TEST A C E B D A E C D B D C
2. TEST E B C C D E A C C E B D
3. TEST A D A D C B E C D C D E
4. TEST A C E B D E C A B E A D
    """,
    "II. Dunya Savasi Sonrasinda Turkiye ve Dunya":"""
    1. TEST A D C E A B C E D A E E
2. TEST D B B A C C D E D D A D
3. TEST D C A E A B B D A E C B
4. TEST E D B C A C A D D C C E
    """,
    "Toplumsal Devrim Caginda Dunya ve Turkiye":"""
    1. TEST E E C E A B A A D A A C
2. TEST A A E B E C C D A B D C
3. TEST E B C E A C D B B C D E
4. TEST E D C B D C E B D D C D
    """,
    "21. Yuzyilin Esiginde Turkiye ve Dunya":"""
    1. TEST E D C D B A D C E B A B
2. TEST D B B A C E B A D E D D
3. TEST D C E A B A B B D E C D
4. TEST A D E E C B E C A D A B
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
son_soru_sayfasi = 308

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
