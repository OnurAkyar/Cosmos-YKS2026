!pip install PyMuPDF
!wget -O tyt-turkce-ogm.pdf https://ogm-large-cdn.eba.gov.tr/ogm-materyal/mebi-konu-ozetleri/tyt-turkce/tyt-turkce.pdf

# 1. Marker'ı kur
!pip install marker-pdf

# 3. Dönüştürme işlemini başlat
!marker_single tyt-turkce.pdf --output_dir ./tyt_turkce_marker


//Colabta farklı hücre
import fitz  # PyMuPDF

# 1. İnternetten indirdiğin orijinal PDF'i aç
orijinal_pdf_yolu = "tyt-turkce-ogm.pdf"
doc = fitz.open(orijinal_pdf_yolu)

# 2. Yeni ve boş bir PDF oluştur
temiz_doc = fitz.open()

# 3. Asıl konuların başladığı sayfayı belirle
# ÖNEMLİ: PyMuPDF'te sayfalar 0'dan başlar. 
# Örneğin PDF'teki asıl konu anlatımı 15. sayfada başlıyorsa buraya 14 yazmalısın.
baslangic_sayfasi = 9 
bitis_sayfasi = len(doc) - 1

# 4. Sadece belirlediğin aralığı yeni PDF'e kopyala
temiz_doc.insert_pdf(doc, from_page=baslangic_sayfasi, to_page=bitis_sayfasi)

# 5. Temizlenmiş PDF'i kaydet
temiz_pdf_yolu = "tyt-turkce.pdf"
temiz_doc.save(temiz_pdf_yolu)

print(f"Gereksiz ilk {baslangic_sayfasi} sayfa atıldı! Temiz PDF hazır.")


//Colabta farklı hücre
import re

def temizle_markdown_resimleri(girdi_dosyasi, cikti_dosyasi):
    # 1. Dosyayı okuyoruz
    with open(girdi_dosyasi, 'r', encoding='utf-8') as f:
        metin = f.read()

    # 2. Markdown resim etiketlerini temizle: ![alt_metin](dosya_yolu.png)
    metin = re.sub(r'!\[.*?\]\(.*?\)', '', metin)

    # 3. HTML resim etiketlerini temizle (Marker bazen bu formatı da kullanabilir): <img src="...">
    metin = re.sub(r'<img[^>]*>', '', metin)
    
    # 4. Marker'ın bazen düz metin olarak bıraktığı ".png" / ".jpg" içeren anlamsız satırları temizle
    metin = re.sub(r'.*\.png.*', '', metin, flags=re.IGNORECASE)
    metin = re.sub(r'.*\.jpg.*', '', metin, flags=re.IGNORECASE)

    # 5. Resimler silindikten sonra oluşan koca koca boş satırları (3 veya daha fazla) standart paragrafa (2 satır) indir
    metin = re.sub(r'\n{3,}', '\n\n', metin)

    # 6. Temizlenmiş pırıl pırıl metni yeni dosyaya kaydediyoruz
    with open(cikti_dosyasi, 'w', encoding='utf-8') as f:
        f.write(metin)

    print(f"Harika! Bütün resim artıkları temizlendi.")
    print(f"Saf bilgi içeren yeni dosyan: '{cikti_dosyasi}' olarak kaydedildi.")

# Fonksiyonu çalıştırıyoruz
temizle_markdown_resimleri('/content/tyt_turkce_marker/tyt-turkce/tyt-turkce.md', '/content/tyt-turkce-temiz.md')
