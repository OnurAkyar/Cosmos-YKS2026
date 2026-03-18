import fitz  # PyMuPDF
import os
import re
import requests

# ================= 1. AYARLAR VE İNDİRME =================
#pdf_url'i kitaba göre güncelle!
pdf_url = "https://ogm-large-cdn.eba.gov.tr/ogm-materyal/konu-pekistirme/ayt/tde/tde.pdf"
pdf_path = "ayt-edebiyat-konu-pekistirme.pdf"
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
    (11, 28, "AYT_Edebiyat", "Giris"),
    (29, 62, "AYT_Edebiyat", "Siir Bilgisi"),
    (63, 74, "AYT_Edebiyat", "Islamiyet Oncesi Turk Siiri - Gecis Donemi Eserleri"),
    (75, 96, "AYT_Edebiyat", "Halk Siiri"),
    (97, 108, "AYT_Edebiyat", "Divan Siiri"),
    (109, 120, "AYT_Edebiyat", "Tanzimat Donemi Siiri"),
    (121, 132, "AYT_Edebiyat", "Servetifunun Donemi Siiri"),
    (133, 144, "AYT_Edebiyat", "Fecriati Donemi Siiri ve Milli Edebiyat Siiri"),
    (145, 156, "AYT_Edebiyat", "Cumhuriyetin Ilk Yillarinda Siir, Turkiye Disinda Cagdas Turk Siiri"),
    (157, 168, "AYT_Edebiyat", "Cumhuriyet Doneminde Saf Siir, Cumhuriyet Doneminde Toplumcu Siir"),
    (169, 180, "AYT_Edebiyat", "Milli Edebiyat Anlayisini Yansitan Siir, Garip Hareketi, II. Yeni Siiri"),
    (181, 192, "AYT_Edebiyat", "Dini Degerleri, Gelenege Duyarligi ve Metafizik Anlayisi One Cikaran Siir, 1960 Sonrasi Toplumcu Egilimleri Yansitan Siir"),
    (193, 204, "AYT_Edebiyat", "1980 Sonrasi Turk Siiri, Cumhuriyet Sonrasi Halk Siiri"),
    (205, 216, "AYT_Edebiyat", "Masal - Fabl"),
    (217, 228, "AYT_Edebiyat", "Destan - Efsane"),
    (229, 252, "AYT_Edebiyat", "Hikaye"),
    (253, 262, "AYT_Edebiyat", "Dede Korkut Hikayeleri, Halk Hikayesi, Cenkname, Mesnevi"),
    (263, 274, "AYT_Edebiyat", "Tanzimat, Servetifunun, Fecriati Donemi Hikaye, Milli Edebiyat Donemi Hikaye"),
    (275, 286, "AYT_Edebiyat", "Cumhuriyet Doneminde Hikaye (1923-1940 ve 1940-1960)"),
    (287, 296, "AYT_Edebiyat", "1960 Sonrasi Hikaye ve Kucurek Hikaye"),
    (297, 320, "AYT_Edebiyat", "Roman"),
    (321, 342, "AYT_Edebiyat", "Tanzimat, Servetifunun, Milli Edebiyat Doneminde Roman, Dunya Edebiyatinda Roman"),
    (343, 354, "AYT_Edebiyat", "Cumhuriyet Doneminde Roman (1923-1950)"),
    (355, 366, "AYT_Edebiyat", "1950 Sonrasi Toplumcu Gercekci, Milli-Dini Duyarliliklari Yansitan, Bireyin Ic Dunyasini Esas Alan, Modernist ve Postmodern Roman"),
    (367, 378, "AYT_Edebiyat", "Tiyatro"),
    (379, 390, "AYT_Edebiyat", "Geleneksel Turk Tiyatrosu, Tanzimat, Servetifunun, Fecriati, Milli Edebiyat Donemi Tiyatro"),
    (391, 402, "AYT_Edebiyat", "Cumhuriyet Doneminde Tiyatro (1923-1950)"),
    (403, 414, "AYT_Edebiyat", "1950 Sonrasi Turk Tiyatrosu"),
    (415, 452, "AYT_Edebiyat", "Ogretici Metinler"),
    (453, 464, "AYT_Edebiyat", "Edebi Akimlar")
]

def konu_bul(sayfa_numarasi):
    for baslangic, bitis, ders, konu in konu_haritasi:
        if baslangic <= sayfa_numarasi <= bitis:
            return ders, konu
    return None, None

#jpg fomratını isimlendirmek için eklendi. Kitaba göre güncelle!
# ================= 3. MANUEL CEVAP ANAHTARI ŞABLONU =================
manuel_cevap_anahtari = {
    "Giris": {
        "Test_1": "ACBECEEBEBCC",
        "Test_2": "BBAEDEEEDDEC",
        "Test_3": "DBCCDBECAC",
        "Test_4": "EDEAADCE"
    },
    "Siir Bilgisi": {
        "Test_1": "EDDACABCEBBACA", # 1. TEST - A
        "Test_2": "DABEABECDCCA",   # 1. TEST - B
        "Test_3": "CDBABBACEEE",    # 1. TEST - C
        "Test_4": "EBEDEACBCAAB",   # 2. TEST - A
        "Test_5": "ECDABACA",       # 2. TEST - B
        "Test_6": "BCAAEEEDBDAAD",  # 2. TEST - C
        "Test_7": "CDDCBDACCBE",    # 3. TEST - A
        "Test_8": "ACEDACBEE",      # 3. TEST - B
        "Test_9": "EAEBACDECA",     # 3. TEST - C
        "Test_10": "BDAACEBCED",    # 4. TEST - A
        "Test_11": "ECDADECBC",     # 4. TEST - B
        "Test_12": "DECBDECDB"      # 4. TEST - C
    },
    "Islamiyet Oncesi Turk Siiri - Gecis Donemi Eserleri": {
        "Test_1": "EBDECCCEADAEC",
        "Test_2": "BDEBDABCB",
        "Test_3": "ECCEED",
        "Test_4": "EBDABDBDACC"
    },
    "Halk Siiri": {
        "Test_1": "BEDEBBECCBDACAB",  # 1. TEST - A
        "Test_2": "DADCDCDDDBCEBBDC", # 1. TEST - B
        "Test_3": "CEDECBDBAAED",     # 2. TEST - A
        "Test_4": "ECCDDCABBDB",      # 2. TEST - B
        "Test_5": "CBBDCCADEA",       # 3. TEST - A
        "Test_6": "CEDACEDBDD",       # 3. TEST - B
        "Test_7": "DCABAEBCBBEC",     # 4. TEST - A
        "Test_8": "DEDBCCABECEE"      # 4. TEST - B
    },
    "Divan Siiri": {
        "Test_1": "BDEDCDDACDCECD",
        "Test_2": "DCCDEADBEBEE",
        "Test_3": "DEDDADCAC",
        "Test_4": "ECDBACBABCE"
    },
    "Tanzimat Donemi Siiri": {
        "Test_1": "CBBDADCAAEBDC",
        "Test_2": "CADAAECDAB",
        "Test_3": "DCAAADACDBCC",
        "Test_4": "AAEDDBCDEE"
    },
    "Servetifunun Donemi Siiri": {
        "Test_1": "EACAADDEEAD",
        "Test_2": "CDBAACCDCA",
        "Test_3": "DCCDCDEBAB",
        "Test_4": "EDDADDBDCEE"
    },
    "Fecriati Donemi Siiri ve Milli Edebiyat Siiri": {
        "Test_1": "DABDDCEEDBCE",
        "Test_2": "ABBACAADAE",
        "Test_3": "DDECCAEABA",
        "Test_4": "EDEDEDCEDE"
    },
    "Cumhuriyetin Ilk Yillarinda Siir, Turkiye Disinda Cagdas Turk Siiri": {
        "Test_1": "EDBCEDBBEDDA",
        "Test_2": "BDDCBDADDE",
        "Test_3": "EADCEDCBDEEA",
        "Test_4": "EDDADAABCD"
    },
    "Cumhuriyet Doneminde Saf Siir, Cumhuriyet Doneminde Toplumcu Siir": {
        "Test_1": "ACACAACACE",
        "Test_2": "CCDECDDEB",
        "Test_3": "BCADADABAA",
        "Test_4": "DBCDEBED"
    },
    "Milli Edebiyat Anlayisini Yansitan Siir, Garip Hareketi, II. Yeni Siiri": {
        "Test_1": "DBEDDCCAEEC",
        "Test_2": "EDACEDAECC",
        "Test_3": "CBDEBAEEDA",
        "Test_4": "DBEBAEDCDC"
    },
    "Dini Degerleri, Gelenege Duyarligi ve Metafizik Anlayisi One Cikaran Siir, 1960 Sonrasi Toplumcu Egilimleri Yansitan Siir": {
        "Test_1": "DDEACDCAEB",
        "Test_2": "CEAADBCBDD",
        "Test_3": "BCCBABEEA",
        "Test_4": "BCAEDBCDB"
    },
    "1980 Sonrasi Turk Siiri, Cumhuriyet Sonrasi Halk Siiri": {
        "Test_1": "EBCDEDDAEA",
        "Test_2": "BDBDAEADDA",
        "Test_3": "ADDBCCBCD",
        "Test_4": "CBEDDABC"
    },
    "Masal - Fabl": {
        "Test_1": "DBCEABDACAED",
        "Test_2": "BACDACADBCBD",
        "Test_3": "DEBBCAECDAA",
        "Test_4": "ECBDCBDAC"
    },
    "Destan - Efsane": {
        "Test_1": "CEBBABCEEDEAEBD",
        "Test_2": "BCDDCCCBADA",
        "Test_3": "CBEEBDDEDED",
        "Test_4": "CCDBBADED"
    },
    "Hikaye": {
        "Test_1": "BEEADECADBEE",   # 1. TEST - A
        "Test_2": "EBDCACAEBEBD",   # 1. TEST - B
        "Test_3": "ECACBBADCED",    # 2. TEST - A
        "Test_4": "CBDECABABCDEB",  # 2. TEST - B
        "Test_5": "ACDDECEBAC",     # 3. TEST - A
        "Test_6": "DBEEACA",        # 3. TEST - B
        "Test_7": "CDBEADCBE",      # 4. TEST - A
        "Test_8": "EDCCBB",         # 4. TEST - B
        "Test_9": "AEACAECA"        # 4. TEST - C
    },
    "Dede Korkut Hikayeleri, Halk Hikayesi, Cenkname, Mesnevi": {
        "Test_1": "AEADCDAACDCED",
        "Test_2": "BDDDBCAAAEEBC",
        "Test_3": "AAEDCBCDBAD",
        "Test_4": "CDAECCECEE"
    },
    "Tanzimat, Servetifunun, Fecriati Donemi Hikaye, Milli Edebiyat Donemi Hikaye": {
        "Test_1": "CDDEAEEDDBBD",
        "Test_2": "DDCBCEADDCE",
        "Test_3": "DDBDECEBEC",
        "Test_4": "BABBDAECADB"
    },
    "Cumhuriyet Doneminde Hikaye (1923-1940 ve 1940-1960)": {
        "Test_1": "DCDEABBDDAAC",
        "Test_2": "AEBADEBACAE",
        "Test_3": "CBADBBDCDE",
        "Test_4": "DACECDEAACC"
    },
    "1960 Sonrasi Hikaye ve Kucurek Hikaye": {
        "Test_1": "DEEEACACEDD",
        "Test_2": "EBCDCECDAE",
        "Test_3": "DDCBAACBC",
        "Test_4": "ABCBCDCBA"
    },
    "Roman": {
        "Test_1": "DEBDBCAECBADCE", # 1. TEST - A
        "Test_2": "DBCBAEACEDB",    # 1. TEST - B
        "Test_3": "ACBECBABDCECD",  # 2. TEST - A
        "Test_4": "CECCBBDEDECA",   # 2. TEST - B
        "Test_5": "ADDBAEBECC",     # 3. TEST - A
        "Test_6": "ABEDEADC",       # 3. TEST - B
        "Test_7": "ABDCDCEA",       # 4. TEST - A
        "Test_8": "BBEAED"          # 4. TEST - B
    },
    "Tanzimat, Servetifunun, Milli Edebiyat Doneminde Roman, Dunya Edebiyatinda Roman": {
        "Test_1": "CEDCEEBDAC",     # 1. TEST - A
        "Test_2": "DACECBDAAEEEBA", # 1. TEST - B
        "Test_3": "EDDCACAEC",      # 2. TEST - A
        "Test_4": "ACBEDEBBCCDA",   # 2. TEST - B
        "Test_5": "EEABADEE",       # 3. TEST - A
        "Test_6": "ECEBABAEADC",    # 3. TEST - B
        "Test_7": "BBAADABBDA",     # 4. TEST - A
        "Test_8": "DACBCBDDE"       # 4. TEST - B
    },
    "Cumhuriyet Doneminde Roman (1923-1950)": {
        "Test_1": "EEBBAECBCAC",
        "Test_2": "DBCDDADADEBBE",
        "Test_3": "EBBAACDABADCC",
        "Test_4": "BDEADCDDDBEC"
    },
    "1950 Sonrasi Toplumcu Gercekci, Milli-Dini Duyarliliklari Yansitan, Bireyin Ic Dunyasini Esas Alan, Modernist ve Postmodern Roman": {
        "Test_1": "BCDEACEA",
        "Test_2": "CBEEBCADA",
        "Test_3": "DAEACECD",
        "Test_4": "DCBEACEE"
    },
    "Tiyatro": {
        "Test_1": "DECBADECEAA",
        "Test_2": "ABDEBACDEB",
        "Test_3": "EBBDAAEBC",
        "Test_4": "BEACDDCACD"
    },
    "Geleneksel Turk Tiyatrosu, Tanzimat, Servetifunun, Fecriati, Milli Edebiyat Donemi Tiyatro": {
        "Test_1": "ECABCACBEEDCCBDB",
        "Test_2": "CBCCEEEEDEBED",
        "Test_3": "CAEAAAEBDE",
        "Test_4": "BDACDEEDEC"
    },
    "Cumhuriyet Doneminde Tiyatro (1923-1950)": {
        "Test_1": "DDECACEBDCB",
        "Test_2": "ABABCBDEDE",
        "Test_3": "ACCDBCBCB",
        "Test_4": "BCDBDCBDCD"
    },
    "1950 Sonrasi Turk Tiyatrosu": {
        "Test_1": "DCABBDEACBACD",
        "Test_2": "BDABEDDAEBE",
        "Test_3": "CABACBEEBDDD",
        "Test_4": "EACABECDCBBD"
    },
    "Ogretici Metinler": {
        "Test_1": "BDCDAAACDDEB",
        "Test_2": "CBCCBCBBB",
        "Test_3": "CBBDDAADEC",
        "Test_4": "BDEDBEEDD"
    },
    "Edebi Akimlar": {
        "Test_1": "CDBECDCEC",
        "Test_2": "EECAAECCB",
        "Test_3": "BBDBCBADCE",
        "Test_4": "BBDCEAECDA"
    }
}
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

#Kitabın içerisinde sorular olan son sayfasını belirtir. Kitaba göre güncelle!
son_soru_sayfasi = 464

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

            for satir in blok.get("lines", []):
                satir_metni = ""
                for span in satir.get("spans", []):
                    span_text = span.get("text", "")
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
                ust_metin = tam_metin[:30].upper()

                # Soru numarasının (ilk span) bold olup olmadığını kontrol eden kısım
                bold_mu = ("bold" in ilk_span_font) or (ilk_span_flags & 16)

                if "TEST" not in ust_metin and bold_mu:
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

                        if 0 <= indeks < len(cevap_listesi):
                            dogru_cevap = cevap_listesi[indeks]

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

                    #Soru isimlerini kitaba ve isteğine göre güncelle!
                    dosya_adi = f"question-Ayt_Edebiyat_{soru_no_int}. answer-{dogru_cevap}.jpg"
                    kayit_yolu = os.path.join(hedef_klasor, dosya_adi)

                    pix.save(kayit_yolu)

                except Exception as e:
                    pass

print("İşlem Tamam! Gereksiz kelime filtresi tamamen silindi.")
