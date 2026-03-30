# Sayı Kümeleri

Sayıları yazmak için kullanılan sembollere rakam denir.
Rakamlar kümesi $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$'dur.

- $0, 1, 2, 3, \dots$ şeklindeki sayıların oluşturduğu kümeye doğal sayılar kümesi denir ve $\mathbb{N}$ ile gösterilir. $\mathbb{N} = \{0, 1, 2, 3, \dots\}$ şeklindedir.
- $\mathbb{N}$ doğal sayılar kümesine $-1, -2, -3, \dots$ sayıların eklenmesiyle oluşan sayı kümesine tam sayılar kümesi denir ve $\mathbb{Z}$ ile gösterilir. $\mathbb{Z} = \{\dots, -3, -2, -1, 0, 1, 2, 3, \dots\}$ şeklindedir.
- $a$ ve $b$ tam sayılar, $b$ sıfırdan farklı olmak üzere $\frac{a}{b}$ şeklinde yazılabilen sayılara rasyonel sayılar denir. Rasyonel sayılar kümesi $\mathbb{Q}$ simgesi ile gösterilir.
- $a$ ve $b$ tam sayılar ve $b$ sıfırdan farklı olmak üzere $\frac{a}{b}$ şeklinde yazılamayan sayılara irrasyonel sayılar denir. İrrasyonel sayılar kümesi $\mathbb{Q}'$ simgesi ile gösterilir. İrrasyonel sayılara $\sqrt{2}$, $\sqrt{\frac{3}{5}}$, $\pi$, $\dots$ sayıları örnek olarak verilebilir.

## İrrasyonel Sayılar
- Kök dışına tam olarak çıkamayan sayılardır.
- Virgülden sonraki kısmı tam olarak bilinmeyen sayılardır.
- İki tam sayının oranı şeklinde yazılamayan sayılardır.
- $\sqrt{-2}$, $\sqrt{-9}$ gibi içinde negatif sayı bulunan kareköklü sayılar gerçek sayı belirtmez.
- Rasyonel sayılar kümesi ile irrasyonel sayılar kümesinin birleşiminden oluşan kümeye gerçek (reel) sayılar kümesi denir ve $\mathbb{R}$ simgesi ile gösterilir. Gerçek sayılar kümesinin her elemanına sayı doğrusunda bir nokta karşılık gelir.
- Sayı kümeleri arasında $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$ ilişkisi vardır ve $\mathbb{Q} \cup \mathbb{Q}' = \mathbb{R}$'dir.

## Gerçek Sayıların Sayı Doğrusunda Gösterilmesi
Sayı doğrusu gerçek sayıların bir gösterim şeklidir. Her gerçek sayı, sayı doğrusu üzerinde bir nokta belirtir.

# Temel İşlemler

## Gerçek Sayılar Kümesinde Toplama ve Çarpma İşleminin Özellikleri

Kapalılık Özelliği:
Herhangi iki gerçek sayının toplamı ya da çarpımı yine bir gerçek sayıdır. Her $a, b \in \mathbb{R}$ için $a + b \in \mathbb{R}$ ve $a \cdot b \in \mathbb{R}$'dir.

Değişme Özelliği:
Herhangi iki gerçek sayının toplamında ya da çarpımında sayıların yerlerinin değiştirilmesi sonucu değiştirmez. Her $a, b \in \mathbb{R}$ için $a+b = b+a$ ve $a \cdot b = b \cdot a$'dır.

Birleşme Özelliği:
Herhangi üç gerçek sayının toplamı ya da çarpımında işlem sırası için seçilen gruplamanın belirleniş şekli sonucu değiştirmez. Her $a, b, c \in \mathbb{R}$ için $(a + b) + c = a + (b + c)$ ve $(a \cdot b) \cdot c = a \cdot (b \cdot c)$'dir.

Birim (Etkisiz) Eleman:
Herhangi bir gerçek sayıya 0 eklemek veya herhangi bir gerçek sayı ile 1'i çarpmak sonucu değiştirmez. Toplama işleminin birim elemanı "0" ve çarpma işleminin birim elemanı "1" dir.

Ters Eleman:
Her $a, b \in \mathbb{R}$ ve $b \neq 0$ için, $a + (-a) = (-a) + a = 0$ olduğundan $a$'nın toplama işlemine göre tersi $-a$'dır. $a \cdot \frac{1}{a} = \frac{1}{a} \cdot a = 1$ olduğundan $a$'nın çarpma işlemine göre tersi $\frac{1}{a}$'dır. (0'ın çarpmaya göre tersi yoktur.)

Yutan Eleman:
Herhangi bir gerçek sayı 0 ile çarpıldığında sonuç her zaman 0'dır.

Dağılma Özelliği:
Her $a, b, c \in \mathbb{R}$ için $a \cdot (b + c) = (a \cdot b) + (a \cdot c)$ ve $(a + b) \cdot c = (a \cdot c) + (b \cdot c)$'dir.

## Negatif ve Pozitif Sayılarda Çarpma ve Bölme
- $(+) \cdot (-) = (-)$
- $(-) \cdot (+) = (-)$
- $(+) \cdot (+) = (+)$
- $(-) \cdot (-) = (+)$
- $(+) : (-) = (-)$
- $(-) : (+) = (-)$
- $(+) : (+) = (+)$
- $(-) : (-) = (+)$

Bir pozitif ve bir negatif gerçek sayının toplamının işareti mutlak değerce büyük olan sayının işareti ile aynı olur.

## İşlem Önceliği
1. Üs alınır.
2. Parantez içi işlemler yapılır.
3. Çarpma ve bölme işlemleri yapılır.
4. Toplama ve çıkarma işlemleri yapılır.

Dikkat: Art arda gelen çarpma ve bölme işlemlerinden önce soldaki yapılır.

# Tek ve Çift Sayılar

Çift Sayılar:
2 ile kalansız bölünebilen sayılara çift sayılar denir. $n \in \mathbb{Z}$ olmak üzere çift sayılar $2n$ ile gösterilir. $\{\dots, -4, -2, 0, 2, 4, \dots\}$

Tek Sayılar:
2 ile bölündüğünde 1 kalanını veren sayılara tek sayılar denir. $n \in \mathbb{Z}$ olmak üzere tek sayılar $2n - 1$ ya da $2n + 1$ ile gösterilir. $\{\dots, -3, -1, 1, 3, \dots\}$

| + / - | T | Ç |
|---|---|---|
| T | Ç | T |
| Ç | T | Ç |

| $\times$ | T | Ç |
|---|---|---|
| T | T | Ç |
| Ç | Ç | Ç |

$n \in \mathbb{Z}^+$ olmak üzere, tek sayıların pozitif tam kuvvetleri tek, çift sayıların pozitif tam kuvvetleri çifttir. $T^n = T$, $Ç^n = Ç$.

# Pozitif ve Negatif Sayılar

- Pozitif Sayılar: Sıfırdan büyük olan sayılara pozitif sayılar denir ($a > 0$).
- Negatif Sayılar: Sıfırdan küçük olan sayılara negatif sayılar denir ($a < 0$).
- Sıfır sayısı ne pozitif ne de negatiftir. İşareti yoktur.
- Sayı doğrusunda daima sağdaki sayı solundaki sayıdan büyüktür.

| $a$ | $b$ | $a+b$ |
|---|---|---|
| $(+)$ | $(+)$ | $+$ |
| $(-)$ | $(-)$ | $-$ |
| $|a| < |b|$ ve $a>0, b<0$ | $-$ | $-$ |
| $|a| > |b|$ ve $a>0, b<0$ | $+$ | $+$ |

Çarpma ve Bölme: Aynı işaretli sayıların çarpımı/bölümü pozitif, ters işaretli sayıların çarpımı/bölümü negatif çıkar.
Kuvvetler: Pozitif sayıların bütün kuvvetleri pozitiftir. Negatif sayıların çift kuvvetleri pozitif, tek kuvvetleri negatiftir.

# Ardışık Sayılar

Belirli bir kurala göre art arda gelen sayılara ardışık sayılar denir.
- Ardışık tam sayılar: $n, n+1, n+2, \dots$
- Ardışık çift sayılar: $2n, 2n+2, 2n+4, \dots$
- Ardışık tek sayılar: $2n-1, 2n+1, 2n+3, \dots$

Terim Sayısı ve Toplamı:
- $\text{Terim Sayısı} = \frac{\text{Son Terim} - \text{İlk Terim}}{\text{Ortak Fark}} + 1$
- $\text{Terimlerin Toplamı} = \frac{\text{Son Terim} + \text{İlk Terim}}{2} \cdot \text{Terim Sayısı}$

Özel Toplamlar:
- $1 + 2 + 3 + \dots + n = \frac{n(n+1)}{2}$
- $1 + 3 + 5 + \dots + (2n - 1) = n^2$
- $2 + 4 + 6 + \dots + 2n = n(n + 1)$

# Sayı Basamakları

Bir sayıyı oluşturan rakamlardan her birinin o sayı içerisindeki yerine basamak denir.
$abcde = 10000a + 1000b + 100c + 10d + e$ olarak çözümlenir.
- $AB + BA = 11(A + B)$
- $AB - BA = 9(A - B)$

# Asal ve Aralarında Asal Sayılar

Asal Sayılar:
1 ve kendisinden başka pozitif böleni olmayan 1'den büyük tam sayılara asal sayılar denir. $\{2, 3, 5, 7, 11, 13, \dots\}$
- 2 en küçük asal sayıdır ve tek çift asal sayıdır.
- Ardışık tam sayı olan asal sayılar sadece 2 ve 3'tür.

Aralarında Asal Sayılar:
1'den başka pozitif ortak böleni olmayan pozitif tam sayılara aralarında asal sayılar denir.
- Ardışık tam sayılar aralarında asaldır.
- Ardışık tek tam sayılar aralarında asaldır.

# Bölme İşlemi

$A = B \cdot C + K$
Kalan sayı $K$ olmak üzere; $0 \le K < B$ olmalıdır. $K=0$ ise $A$ sayısı $B$ sayısına tam bölünür.

# Bölünebilme Kuralları

- 2 ile: Birler basamağı çift olmalı.
- 3 ile: Rakamları toplamı 3'ün katı olmalı.
- 4 ile: Son iki basamağı 4'ün katı olmalı.
- 5 ile: Birler basamağı 0 veya 5 olmalı.
- 8 ile: Son üç basamağı 8'in katı olmalı.
- 9 ile: Rakamları toplamı 9'un katı olmalı.
- 10 ile: Birler basamağı 0 olmalı.
- 11 ile: Rakamlar sağdan sola $+$, $-$, $+$, $-$ işaretlenerek toplanır, sonuç 11'in katı olmalı.

Aralarında Asal Sayıların Çarpımına Bölünebilme:
- 6 ile bölünebilme: 2 ve 3'e tam bölünmeli.
- 12 ile bölünebilme: 3 ve 4'e tam bölünmeli.
- 15 ile bölünebilme: 3 ve 5'e tam bölünmeli.
- 36 ile bölünebilme: 4 ve 9'a tam bölünmeli.

# Asal Çarpanlar

Bir $A$ tam sayısının $A = x^a \cdot y^b \cdot z^c$ ($x, y, z$ asal) şeklinde ifade edilmesine asal çarpanlara ayırma denir.
- Pozitif Bölen Sayısı (PBS) = $(a+1) \cdot (b+1) \cdot (c+1)$
- Tam Sayı Bölen Sayısı = $2 \cdot (a+1) \cdot (b+1) \cdot (c+1)$

# EBOB ve EKOK

- EBOB (En Büyük Ortak Bölen): Ortak bölenlerin en büyüğü. Ortak asal çarpanlardan üssü küçük olanlar çarpılır.
- EKOK (En Küçük Ortak Kat): Ortak katların en küçüğü. Ortak asallardan üssü büyük olanlar ve ortak olmayanların hepsi çarpılır.
- $a \cdot b = \text{EBOB}(a, b) \cdot \text{EKOK}(a, b)$
- Aralarında asal sayılar için: $\text{EBOB}(a, b) = 1$, $\text{EKOK}(a, b) = a \cdot b$.

# Rasyonel, Ondalık ve Devirli Sayılar

- Rasyonel Toplama/Çıkarma: Paydalar EKOK'larında eşitlenir.
- Rasyonel Çarpma/Bölme: Tam sayılı kesirler bileşik kesre çevrilir. Bölmede ikinci kesir ters çevrilip çarpılır.
- Devirli Ondalık Sayılar: $\frac{\text{Sayının Tamamı} - \text{Devretmeyen Kısım}}{\text{Virgülden Sonra Devreden Kadar 9, Devretmeyen Kadar 0}}$

# Basit Eşitsizlikler

- Eşitsizliğin her iki tarafı negatif bir sayıyla çarpılır veya bölünürse eşitsizlik yön değiştirir.
- Aynı yönlü eşitsizlikler taraf tarafa toplanabilir (fakat çıkarılamaz).
- $0 < a < b$ iken $\frac{1}{a} > \frac{1}{b}$ olur.

# Mutlak Değer

Bir sayının başlangıç noktasına (sıfıra) olan uzaklığıdır. Uzaklık negatif olamayacağından $|x| \ge 0$'dır.
- $x > 0$ ise $|x| = x$
- $x < 0$ ise $|x| = -x$
- $|x \cdot y| = |x| \cdot |y|$
- $|x + y| \le |x| + |y|$ (Üçgen eşitsizliği)
- $|x| \le a \Leftrightarrow -a \le x \le a$
- $|x| \ge a \Leftrightarrow x \le -a$ veya $x \ge a$

# Üslü İfadeler

$a^n = a \cdot a \cdot \dots \cdot a$ ($n$ tane)
- $x^{-n} = \frac{1}{x^n}$
- $x^a \cdot x^b = x^{a+b}$
- $\frac{x^a}{x^b} = x^{a-b}$
- $(x^a)^b = x^{a \cdot b}$
- $x^0 = 1$ ($x \neq 0$)

# Köklü İfadeler

$x^n = a$ eşitliğini sağlayan $x$ değerine $a$'nın $n$. kuvvetten kökü denir ($x = \sqrt[n]{a}$).
- $n$ çift ise $a \ge 0$ olmalıdır. $\sqrt[n]{x^n} = |x|$ olarak çıkar.
- $n$ tek ise $\sqrt[n]{x^n} = x$ olarak çıkar.
- $\sqrt[n]{a} \cdot \sqrt[n]{b} = \sqrt[n]{a \cdot b}$
- Eşlenik: Paydayı kökten kurtarmak için rasyonel yapan çarpanla çarpılır. $\sqrt{a}-\sqrt{b}$ eşleniği $\sqrt{a}+\sqrt{b}$'dir.

# Oran ve Orantı

$\frac{a}{b} = \frac{c}{d} = k$ ($k$: orantı sabiti)
- Doğru Orantı: Biri artarken diğeri de aynı oranda artar. ($\frac{a}{b} = k$)
- Ters Orantı: Biri artarken diğeri azalır. ($a \cdot b = k$)

# Problemler

- Yaş Problemleri: İki kişi arasındaki yaş farkı zamanla değişmez.
- İşçi Problemleri: Bir işçi işin tamamını $x$ günde yapıyorsa, $a$ günde işin $\frac{a}{x}$'ini yapar.
- Kâr-Zarar: Kâr/Zarar maliyet üzerinden, indirim/zam satış fiyatı üzerinden hesaplanır.
- Hareket: $X = V \cdot t$ (Yol = Hız $\cdot$ Zaman).
- Karışım: $\text{Saf Madde Yüzdesi} = \frac{\text{Saf Madde Miktarı}}{\text{Tüm Karışım}} \cdot 100$.

# Mantık (Önermeler)

Doğru ya da yanlış kesin bir hüküm bildiren ifadelere önerme denir.
- "Ve" ($\land$) Bağlacı: Her iki önerme doğru ise doğru, diğer durumlarda yanlıştır.
- "Veya" ($\lor$) Bağlacı: En az biri doğru ise doğru, her ikisi yanlış ise yanlıştır.
- "Ya da" ($\veebar$) Bağlacı: Önermelerin doğruluk değerleri farklı ise doğru, aynı ise yanlıştır.
- "İse" ($\Rightarrow$) Bağlacı: Birincisi doğru, ikincisi yanlış iken yanlış, diğer durumlarda doğrudur.
- "Ancak ve Ancak" ($\Leftrightarrow$): Doğruluk değerleri aynı iken doğru, farklı iken yanlıştır.
- De Morgan: $(p \lor q)' \equiv p' \land q'$ ve $(p \land q)' \equiv p' \lor q'$

# Kümeler

- $A \subset B$: A'nın her elemanı B'nin de elemanıysa A, B'nin alt kümesidir.
- Alt küme sayısı $2^n$, öz alt küme sayısı $2^n - 1$'dir.
- $s(A \cup B) = s(A) + s(B) - s(A \cap B)$
- $A - B$ veya $A \setminus B$: A'da olup B'de olmayan elemanlar.
- Kartezyen Çarpım: $A \times B = \{(a, b) \mid a \in A \text{ ve } b \in B\}$. Eleman sayısı $s(A \times B) = s(A) \cdot s(B)$'dir.

# Sayma, Permütasyon ve Kombinasyon

- Saymanın Temel İlkesi (Çarpma Kuralı): $n_1 \cdot n_2 \cdot \dots \cdot n_k$
- Faktöriyel: $n! = n \cdot (n-1) \cdot \dots \cdot 1$. (Not: $0! = 1$)
- Permütasyon (Sıralama): $P(n, r) = \frac{n!}{(n-r)!}$
- Tekrarlı Permütasyon: $\frac{n!}{n_1! \cdot n_2! \cdot \dots \cdot n_r!}$
- Kombinasyon (Seçme): $C(n, r) = \binom{n}{r} = \frac{n!}{r! \cdot (n-r)!}$
- Binom Açılımı: $(x+y)^n = \sum \binom{n}{r} x^{n-r} y^r$. Terim sayısı $n+1$'dir.
- Olasılık: $P(A) = \frac{s(A)}{s(E)} = \frac{\text{İstenen Durum Sayısı}}{\text{Tüm Durumların Sayısı}}$

# Fonksiyonlar

$f: A \to B$, A tanım kümesi, B değer kümesi. Tanım kümesindeki her eleman değer kümesinde yalnız bir elemanla eşleşmelidir.
- Bire Bir Fonksiyon: Tanım kümesindeki her elemanın görüntüsü farklıdır.
- Örten Fonksiyon: Değer kümesinde açıkta eleman kalmaz.
- Sabit Fonksiyon: $f(x) = c$.
- Birim Fonksiyon: $f(x) = x$.
- Doğrusal Fonksiyon: $f(x) = ax + b$.
- Tek/Çift Fonksiyon: $f(-x) = f(x)$ ise çift (y-eksenine simetrik), $f(-x) = -f(x)$ ise tek (orijine simetrik) fonksiyondur.
- Bileşke: $(g \circ f)(x) = g(f(x))$.
- Ters Fonksiyon: $y=f(x) \Leftrightarrow x=f^{-1}(y)$. $f(x) = \frac{ax+b}{cx+d}$ ise $f^{-1}(x) = \frac{-dx+b}{cx-a}$.

# Polinomlar

$P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$. (Üsler doğal sayı olmalıdır).
- Sabit Terim: $x=0$ yazılarak bulunur.
- Katsayılar Toplamı: $x=1$ yazılarak bulunur.
- Çarpanlara Ayırma (Tam Kare): $(a \pm b)^2 = a^2 \pm 2ab + b^2$.
- İki Kare Farkı: $a^2 - b^2 = (a-b)(a+b)$.
- İki Küp Toplamı/Farkı: $a^3 \pm b^3 = (a \pm b)(a^2 \mp ab + b^2)$.
- Kalan Bulma: $P(x)$'in $x-a$ ile bölümünden kalan $P(a)$'dır.

# İkinci Dereceden Denklemler

$ax^2 + bx + c = 0$
- Diskriminant: $\Delta = b^2 - 4ac$.
- Kökler: $x_{1,2} = \frac{-b \pm \sqrt{\Delta}}{2a}$.
- $\Delta > 0$ iki farklı gerçek kök, $\Delta = 0$ çakışık gerçek kök, $\Delta < 0$ gerçek kök yok (karmaşık kök var).
- Kökler Toplamı: $x_1 + x_2 = -\frac{b}{a}$.
- Kökler Çarpımı: $x_1 \cdot x_2 = \frac{c}{a}$.
- Karmaşık Sayılar: $i = \sqrt{-1}$ ($i^2 = -1$). $z = a + bi$'nin eşleniği $\bar{z} = a - bi$'dir.

# İstatistik

- Aritmetik Ortalama: Veri toplamının veri sayısına bölümüdür.
- Mod (Tepe Değer): En çok tekrar eden veri.
- Medyan (Ortanca): Sıralı verilerde tam ortadaki veri.
- Açıklık: En büyük değer ile en küçük değerin farkı.
- Standart Sapma: Verilerin ortalamadan ne kadar saptığının (yayılımının) ölçüsüdür.

# Geometri

Açılar:
- Tümler açılar toplamı $90^\circ$, bütünler açılar toplamı $180^\circ$'dir.

Üçgenler:
- İç açılar toplamı $180^\circ$, dış açılar toplamı $360^\circ$'dir.
- Üçgen Eşitsizliği: $|b-c| < a < b+c$.
- Eşlik ve Benzerlik: K.A.K., A.K.A., K.K.K. kuralları. Benzerlik oranının karesi alanlar oranına eşittir.
- Açıortay: İç açıortay teoremi $\frac{c}{b} = \frac{m}{n}$. Açıortay üzerinden kollara inilen dikmeler eşittir.
- Kenarortay: Ağırlık merkezi kenara $k$, köşeye $2k$ oranında ayırır.
- Pisagor: $a^2 + b^2 = c^2$.
- Öklid (Dikten inen dik): $h^2 = p \cdot k$, $c^2 = p \cdot a$, $b^2 = k \cdot a$.
- Alan: $A = \frac{\text{Taban} \cdot \text{Yükseklik}}{2}$.

Çokgenler ve Dörtgenler:
- $n$ kenarlı çokgenin iç açılar toplamı $(n-2) \cdot 180^\circ$'dir. Dış açılar toplamı $360^\circ$'dir.
- Düzgün çokgenin bir dış açısı $\frac{360^\circ}{n}$'dir.
- Yamuk Alanı: $\frac{\text{Alt Taban} + \text{Üst Taban}}{2} \cdot h$. Orta taban = $\frac{a+c}{2}$.
- Paralelkenar: Karşılıklı kenarlar eşit ve paralel. Alan = $a \cdot h_a$.
- Eşkenar Dörtgen: Köşegenler dik kesişir. Alan = $\frac{|AC| \cdot |BD|}{2}$.
- Deltoid: İkişer kenarı eşit olan dörtgen. Köşegenler dik kesişir.

Katı Cisimler:
- Prizmalar: Hacim = Taban Alanı $\times$ Yükseklik.
- Küp: Alan = $6a^2$, Hacim = $a^3$. Cisim köşegeni = $a\sqrt{3}$.
- Piramitler: Hacim = $\frac{\text{Taban Alanı} \cdot \text{Yükseklik}}{3}$.
