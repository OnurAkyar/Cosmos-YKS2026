# Fonksiyonun Grafikleri İle İlgili Uygulamalar

İki değişken arasında doğrusal bir ilişki varsa, bu ilişki $y = ax + b$ biçimindeki bir doğrusal fonksiyon veya bu fonksiyonun grafiği ile ifade edilebilir. Burada $a$ ve $b$ gerçek sayılardır. Doğrusal fonksiyonlar, değişkenler arasındaki sabit oranlı değişimi modellemek için kullanılır. Örneğin, bir arabanın deposunda kalan yakıt miktarı ile alınan yol arasında doğrusal bir ilişki vardır; her kilometrede eşit miktarda yakıt tüketilir.

Geçtiği bir nokta ve eğimi bilinen doğrunun denklemini bulmak için önce eğim kavramını anlamak gerekir. Bir $d$ doğrusunun $x$ ekseni ile pozitif yönde yaptığı açı $\alpha$ olsun. Bu $\alpha$ açısının tanjant değeri, doğrunun eğimine eşittir. Bir dik üçgende bir açının tanjantı, karşı dik kenar uzunluğunun komşu dik kenar uzunluğuna oranı olduğundan, doğrunun eğimi $m = \tan \alpha = \frac{y_2 - y_1}{x_2 - x_1}$ olarak hesaplanır. Bu formülün mantığı, doğru üzerinde iki nokta alındığında, dikey değişimin yatay değişime oranının her iki nokta için aynı olması ve bu oranın doğrunun eğimini vermesidir. Eğimi $m$ olan ve $A(x_0, y_0)$ noktasından geçen doğrunun denklemi ise $y - y_0 = m \cdot (x - x_0)$ formülü ile bulunur. Bu formül, doğru üzerindeki herhangi bir noktanın koordinatlarının bu eğim ilişkisini sağlaması gerektiği düşüncesiyle türetilmiştir: $(y - y_0)/(x - x_0) = m$ olduğundan içler dışlar çarpımı yapılır.

Aralarında doğru veya ters orantı bulunan çoklukların ortak çözümlerinde doğrusal fonksiyonlar sıklıkla kullanılır. Örneğin, gelir-gider dengesi, bir aracın deposunda kalan yakıt miktarı ile aldığı yol arasındaki ilişki, bir ürünün alış ve satış fiyatı arasındaki fark gibi günlük hayattaki birçok durum doğrusal fonksiyonlarla modellenebilir. Daha soyut bir örnek vermek gerekirse, $4 \cdot 7$ işlemi istendiğinde zihnimizde beliren $28$ sayısı da beynin bir fonksiyonudur. Matematikte fonksiyon kavramı, tıpkı günlük hayatta gözlemlediğimiz neden-sonuç ilişkileri gibi, bir girdiyi belirli bir kurala göre bir çıktıya dönüştüren bir yapıdır.

# Fonksiyonun Eksenleri Kestiği Noktalar

Bir $y = f(x)$ fonksiyonunun $x$ eksenini kestiği noktalar, $y = 0$ için $f(x) = 0$ denkleminin gerçek kökleridir. Yani bu noktalar, fonksiyonun sıfır olduğu yerlerdir. Bunun nedeni, $x$ ekseni üzerindeki tüm noktaların ordinatının sıfır olmasıdır; dolayısıyla grafiğin $x$ eksenini kestiği noktada $y=0$ olmalıdır. $y = f(x)$ fonksiyonunun $y$ eksenini kestiği noktalar ise $x = 0$ için $y = f(0)$ değerini verir. Çünkü $y$ ekseni üzerindeki noktaların apsisi sıfırdır. $y = f(x)$ bir polinom fonksiyon olduğunda, sabit terim doğrudan fonksiyonun $y$ eksenini kestiği noktanın ordinatına eşittir. İkinci dereceden $f(x) = ax^2 + bx + c$ fonksiyonları $y$ eksenini mutlaka bir noktada keser ve bu nokta $(0, c)$ olur. Bu, $x=0$ yazıldığında $f(0)=c$ çıkmasından kaynaklanır. Eksen kesişimlerini bilmek, bir fonksiyonun grafiğini kabaca çizerken ilk adımdır.

Fonksiyonun negatif ve pozitif olduğu aralıklar, grafiğin $x$ ekseninin altında mı yoksa üstünde mi olduğunu gösterir. $f: \mathbb{R} \to \mathbb{R}$, $y = f(x)$ fonksiyonu verilsin. Eğer tanım kümesindeki her $x$ için $f(x) < 0$ ise $f$ fonksiyonu negatif değerlidir ve grafiği tamamen $x$ ekseninin altında kalır. Eğer her $x$ için $f(x) > 0$ ise fonksiyon pozitif değerlidir ve grafiği $x$ ekseninin üstündedir. Bir grafik incelenirken, fonksiyonun pozitif olduğu aralıklar grafiğin $x$ ekseninin üstünde kaldığı aralıklar, negatif olduğu aralıklar ise altında kaldığı aralıklardır. Örneğin, grafiği verilen bir $y = f(x)$ fonksiyonunun pozitif değerler aldığı aralık $(a, d) \cup (b, c)$, negatif değerler aldığı aralık ise $(-\infty, a) \cup (d, b) \cup (c, \infty)$ şeklinde olabilir. Bu aralıklar, grafiğin $x$ eksenini kestiği noktalar arasında işaretin değişip değişmediğine bakılarak belirlenir. İşaret değişimi, tek katlı köklerde gerçekleşir; çift katlı köklerde grafik eksene teğet olur ve işaret değişmez.

# Fonksiyonun Artan veya Azalan Olduğu Aralıklar

Bir fonksiyonun artan veya azalan olduğu aralıklar, onun davranışını anlamada temel bir rol oynar. $f: [a, b] \to \mathbb{R}$ şeklinde tanımlı bir $f(x)$ fonksiyonu düşünelim. Eğer $[a, b]$ aralığındaki herhangi iki $x_1 < x_2$ sayısı için $f(x_1) < f(x_2)$ oluyorsa, $f(x)$ fonksiyonu bu aralıkta artandır. Bu, $x$ büyüdükçe $f(x)$'in de büyüdüğü anlamına gelir ve değişkenler arasında aynı yönlü bir ilişki olduğunu gösterir. Eğer $x_1 < x_2$ iken $f(x_1) > f(x_2)$ oluyorsa, $f(x)$ fonksiyonu azalandır. Bu durumda $x$ büyüdükçe $f(x)$ küçülür, yani ters yönlü bir ilişki vardır. Eğer $x_1 < x_2$ iken $f(x_1) = f(x_2)$ oluyorsa, $f(x)$ fonksiyonu sabittir; bu durumda değişken değişse bile fonksiyon değeri aynı kalır.

Fonksiyonun maksimum ve minimum değerleri, bir fonksiyonun en yüksek ve en düşük noktalarını belirler. $f: [a, b] \to \mathbb{R}$ verilsin. Eğer aralıktaki tüm $x$ değerleri için $f(x) \ge f(n)$ olacak şekilde bir $n \in [a, b]$ sayısı varsa, $(n, f(n))$ noktasına bir minimum nokta, $f(n)$ değerine de $f$ fonksiyonunun minimum değeri denir. Benzer şekilde, tüm $x$ için $f(x) \le f(m)$ olacak şekilde bir $m \in [a, b]$ varsa, $(m, f(m))$ noktasına bir maksimum nokta, $f(m)$ değerine de maksimum değer denir. Bir fonksiyonun birden fazla yerel maksimum veya minimumu olabilir; burada tanımlanan genellikle mutlak (global) maksimum ve minimumdur. Bu kavramlar, bir fonksiyonun en yüksek ve en düşük değerlerini bulmada kullanılır ve optimizasyon problemlerinin temelini oluşturur.

# Ortalama Değişim Hızı

Ortalama değişim hızı, bir fonksiyonun belirli bir aralıktaki ortalama eğimini ölçer. Bir $f$ fonksiyonunun $[a, b]$ aralığındaki ortalama değişim hızı, fonksiyonun grafiğini $(a, f(a))$ ve $(b, f(b))$ noktalarında kesen doğrunun eğimidir. Bu eğim, $x$ değiştiğinde $f(x)$'in ortalama olarak ne kadar hızlı değiştiğini gösterir. $y = f(x)$ fonksiyonunun bu aralıktaki ortalama değişim hızı şu formülle hesaplanır:
\[
\text{Ortalama değişim hızı} = \frac{f(b) - f(a)}{b - a}.
\]
Bu ifade, $x$ ekseni ile pozitif yönde $\alpha$ açısı yapan kesen doğrunun eğimi $\tan \alpha$'ya eşittir. Doğrusal bir $f(x) = ax + b$ fonksiyonunun eğimi sabit olduğu için ($a$), herhangi bir aralıktaki ortalama değişim hızı da $a$ olur. Bu, doğrusal fonksiyonlarda değişim hızının sabit olduğu anlamına gelir. Artan fonksiyonların ortalama değişim hızı pozitif, azalan fonksiyonlarınki ise negatiftir. Bu işaret, fonksiyonun artan mı yoksa azalan mı olduğu hakkında bilgi verir. Ortalama değişim hızı, daha sonra anlık değişim hızı olan türev kavramına giden yolda önemli bir adımdır.

# İkinci Dereceden Bir Değişkenli Fonksiyonun Grafiği

$a \neq 0$ ve $a, b, c \in \mathbb{R}$ olmak üzere, gerçek sayılar kümesinde $f(x) = ax^2 + bx + c$ şeklinde tanımlanan fonksiyona ikinci dereceden bir değişkenli fonksiyon denir. Bu fonksiyonun grafiğine parabol adı verilir. $a > 0$ olduğunda parabolün kolları yukarı doğru açılır; bu durumda fonksiyonun bir minimum değeri vardır. $a < 0$ olduğunda ise kollar aşağı doğru açılır ve fonksiyon bir maksimum değere sahip olur. Parabolün şekli, $|a|$ büyüdükçe kolların birbirine daha çok yaklaşması (daha dar bir parabol) şeklinde değişir. Bunun nedeni, $|a|$ arttıkça ikinci dereceden terimin etkisinin daha baskın hale gelmesidir. Örneğin, $f(x) = ax^2$ parabolünde $|a|$ arttıkça grafik $y$ eksenine doğru daralır. Parabol, günlük hayatta birçok yerde karşımıza çıkar: bir topun havada izlediği yol, bir çanak antenin şekli, asma köprülerin ana kabloları gibi.

# Tepe Noktası, Simetri Ekseni ve Görüntü Kümesi

Bir parabolün en önemli özelliklerinden biri tepe noktasıdır. $a \neq 0$ olmak üzere $f(x) = ax^2 + bx + c$ parabolünün tepe noktası $T(r, k)$ ile gösterilir. Bu nokta, parabolün yön değiştirdiği (artan iken azalan veya azalan iken artan hale geçtiği) noktadır. Tepe noktasının apsisi $r = -\frac{b}{2a}$ formülüyle bulunur. Bu formül, türev alınarak da elde edilebilir: $f'(x) = 2ax + b = 0$ denkleminin çözümü $x = -\frac{b}{2a}$'dır. Ordinat ise $k = f(r) = \frac{4ac - b^2}{4a}$ olur. $x = r$ doğrusuna parabolün simetri ekseni denir; parabol bu doğruya göre simetriktir. Simetrinin nedeni, ikinci dereceden fonksiyonun $x$'e göre ikinci dereceden olması ve tepe noktasının simetri merkezi olmasıdır. Parabolün en büyük veya en küçük değeri $k$'dir ($a < 0$ ise en büyük, $a > 0$ ise en küçük değer). Görüntü kümesi, $a > 0$ için $[k, \infty)$, $a < 0$ için $(-\infty, k]$ olur.

$ax^2 + bx + c = 0$ denkleminin kökleri $\Delta = b^2 - 4ac$ olmak üzere $x_{1,2} = \frac{-b \pm \sqrt{\Delta}}{2a}$ ile bulunur. Bu kökler, parabolün $x$ eksenini kestiği noktaların apsisleridir. Diskriminantın durumuna göre üç farklı durum ortaya çıkar. Eğer $\Delta < 0$ ise denklemin gerçek kökü yoktur, parabol $x$ eksenini kesmez. Bu durumda parabol tamamen $x$ ekseninin üstünde (a>0) veya altındadır (a<0). Eğer $\Delta = 0$ ise denklemin eşit iki kökü vardır, parabol $x$ eksenine teğettir. Eğer $\Delta > 0$ ise denklemin iki farklı gerçek kökü vardır, parabol $x$ eksenini iki farklı noktada keser. Bu ayrım, ikinci dereceden bir fonksiyonun grafiğinin $x$ ekseni ile ilişkisini anlamak için temeldir ve eşitsizliklerin çözümünde doğrudan kullanılır.

# Parabolün Grafik Çizimi

$f(x) = ax^2 + bx + c$ parabolünü çizmek için tepe noktası ve eksenleri kestiği noktalar bulunur. Tepe noktası $T(r, k)$ biliniyorsa, parabol $f(x) = a(x - r)^2 + k$ biçiminde yazılabilir. Bu form, kareye tamamlama yöntemiyle elde edilir ve parabolün tepe noktasını doğrudan verir. Ayrıca, $x_1$ ve $x_2$ kökler biliniyorsa, $f(x) = a(x - x_1)(x - x_2)$ şeklinde çarpanlarına ayrılmış form kullanılır. Bu form, köklerin nerede olduğunu açıkça gösterir. Çizim yaparken önce tepe noktası işaretlenir, sonra parabolün kollarının yönü ($a$'nın işareti) belirlenir ve varsa $x$ eksenini kestiği noktalar ile $y$ eksenini kestiği $(0, c)$ noktası eklenir. Bu adımlar, parabolün şeklini doğru bir şekilde çizmeyi sağlar. Ayrıca, $x$ eksenine göre simetri olduğu için tepe noktasının sağındaki ve solundaki noktalar simetrik olarak yerleştirilir.

# Bazı Elemanları Verilen Parabol Denklemini Yazma

Bir parabolün denklemini yazmak için yeterli sayıda bilgiye ihtiyaç vardır. Farklı durumlar şöyle ele alınır. Tepe noktası $T(r, k)$ ve geçtiği bir $A(x_0, y_0)$ noktası biliniyorsa, parabolün tepe noktası formu $f(x) = a(x - r)^2 + k$ kullanılır. $A$ noktası yerine yazılarak $a$ bulunur. Bu yöntem, tepe noktasının bilinmesinin parabolün şeklini belirlemede ne kadar güçlü olduğunu gösterir; sadece ölçeklendirme faktörü $a$ bilinmez. $x$ eksenini kestiği noktalar $x_1$, $x_2$ ve geçtiği bir $A(x_0, y_0)$ noktası biliniyorsa, çarpan formu $f(x) = a(x - x_1)(x - x_2)$ kullanılır. $A$ noktası yerine yazılarak $a$ bulunur. Bu durumda, kökler bilindiği için parabolün $x$ eksenini nerede kestiği kesindir; sadece dikey ölçeklendirme faktörü $a$'nın belirlenmesi gerekir. Herhangi üç nokta (tepe noktası veya kesim noktası olması gerekmez) biliniyorsa, bu üç nokta $f(x) = ax^2 + bx + c$ denkleminde yerine yazılarak üç bilinmeyenli ($a, b, c$) üç denklem elde edilir. Bu sistem yok etme veya yerine koyma yöntemiyle çözülür. Bu yöntem, herhangi bir parabolün üç noktadan geçtiği için benzersiz bir şekilde belirlendiği gerçeğine dayanır. Bu, genel olarak $n$ noktadan $n-1$ dereceden bir polinom geçtiği gerçeğinin özel bir durumudur.

# Parabol İle Doğrunun Birbirine Göre Durumları

$f(x) = ax^2 + bx + c$ parabolü ile $y = mx + n$ doğrusu verilsin. Ortak noktaları bulmak için denklemler eşitlenir: $ax^2 + bx + c = mx + n$. Bu düzenlenerek $ax^2 + (b - m)x + (c - n) = 0$ ikinci derece denklemi elde edilir. Bu denklemin diskriminantı $\Delta$'ya göre üç durum oluşur. Eğer $\Delta < 0$ ise denklemin gerçek kökü yoktur; parabol ile doğru kesişmez. Geometrik olarak, doğru parabolün tamamen dışından geçer. Eğer $\Delta = 0$ ise denklemin çift kat kökü vardır; parabol ile doğru bir noktada kesişir, yani doğru parabole teğettir. Teğetlik, doğrunun parabole sadece bir noktada dokunduğu anlamına gelir. Eğer $\Delta > 0$ ise denklemin iki farklı gerçek kökü vardır; parabol ile doğru iki farklı noktada kesişir. Bu durumda doğru parabolün içinden geçer. Ayrıca, bir parabolün dışındaki bir doğruya en yakın noktasını bulmak için, verilen doğruya paralel ve parabole teğet bir doğru çizilir; teğet noktası en yakın noktadır. Bu yöntem, optimizasyon problemlerinde sıkça kullanılır. Özel olarak, $f(x) = ax^2 + bx + c$ parabolüne orijinden çizilen teğetler birbirine dik ise $\Delta = -1$; parabolün $x$ eksenini kestiği noktalardan çizilen teğetler birbirine dik ise $\Delta = 1$ olur. Bu ilişkiler, teğetlerin eğimlerinin çarpımının -1 olması koşulundan türetilir.

# İkinci Dereceden Fonksiyonlarla Modellenen Problemler

$f(x) = ax^2 + bx + c$ parabolünün tepe noktası $T(r, k)$ olduğunda, $r = -\frac{b}{2a}$ ve $k = f(r)$'dir. $a > 0$ ise parabolün en küçük değeri $k$'dir; $a < 0$ ise en büyük değeri $k$'dir. Bu özellik, birçok gerçek hayat probleminin modellenmesinde kullanılır. Örneğin, asma köprülerin ana direkleri arasındaki halatlar (sarkma) $a > 0$ olan parabollere benzer. Bunun nedeni, halatların kendi ağırlıklarıyla aşağı doğru sarkması ve bu şeklin bir parabole çok yakın olmasıdır. Su kemerlerinin kemerleri ise $a < 0$ olan parabollere örnektir. Paraboller, fizikte atış hareketlerinde (mermi yörüngesi), ekonomide kar maksimizasyonu problemlerinde (gelir ve maliyet fonksiyonları ikinci dereceden olabilir) ve mühendislikte optimizasyon problemlerinde yaygın olarak kullanılır.

# Fonksiyonda Uygulamalar

Çift ve tek fonksiyonlar, simetri özellikleriyle öne çıkar. Bir $f(x)$ fonksiyonu, eğer her $x$ için $f(-x) = f(x)$ ise çift fonksiyondur. Çift fonksiyonların grafikleri $y$ eksenine göre simetriktir ve fonksiyonda sadece çift dereceli terimler bulunur. Bu simetri, $x$ ve $-x$'in aynı çıktıyı vermesinden kaynaklanır. Örneğin, $f(x) = x^2$ bir çift fonksiyondur. Eğer $f(-x) = -f(x)$ ise tek fonksiyondur. Tek fonksiyonların grafikleri orijine göre simetriktir ve fonksiyonda sadece tek dereceli terimler bulunur. Bu durumda, $x$ ve $-x$ zıt işaretli çıktılar verir. Örneğin, $f(x) = x^3$ bir tek fonksiyondur. Fonksiyonlarda simetri dönüşümleri, bir grafiğin yansımasını elde etmeyi sağlar. $y = f(x)$ fonksiyonunun $x$ eksenine göre simetriği $y = -f(x)$ ile, $y$ eksenine göre simetriği $y = f(-x)$ ile, orijine göre simetriği ise $y = -f(-x)$ ile verilir. Bu dönüşümler, grafik üzerinde yansımalar yaparak yeni fonksiyonlar elde etmeyi sağlar. Fonksiyonlarda öteleme, grafiğin yerini değiştirir. $k \in \mathbb{R}^+$ olmak üzere, $y = f(x)$ fonksiyonunun $y$ ekseni boyunca $k$ birim yukarı ötelenmesi $y = f(x) + k$, aşağı ötelenmesi $y = f(x) - k$ ile elde edilir. $x$ ekseni boyunca $k$ birim sağa ötelenmesi $y = f(x - k)$, sola ötelenmesi $y = f(x + k)$ ile elde edilir. Bu ötelemeler, fonksiyonun grafiğini kaydırarak aynı şekli korur; sadece konumunu değiştirir. Gerilme ve sıkıştırma dönüşümleri ise grafiğin şeklini değiştirir. $0 < k < 1$ için $y = f(kx)$ grafiği $y$ eksenine göre yatay olarak açar (gerer). Bunun nedeni, $x$'in daha küçük değerlerinin aynı $f$ değerini vermesidir. $k > 1$ için $y = f(kx)$ grafiği $y$ eksenine doğru yatay olarak sıkıştırır. $0 < k < 1$ için $y = k f(x)$ grafiği $x$ eksenine göre dikey olarak sıkıştırır. $k > 1$ için $y = k f(x)$ grafiği $x$ eksenine göre dikey olarak gerer. Bu dönüşümler, fonksiyonun genliğini veya periyodunu değiştirir.

# İkinci Dereceden İki Bilinmeyenli Denklem Sistemi

$a, b, c, d, e, f$ birer gerçek sayı ve $a, b, c$'den en az ikisi sıfırdan farklı olmak üzere $ax^2 + by^2 + cxy + dx + ey + f = 0$ biçimindeki denklemlere ikinci dereceden iki bilinmeyenli denklem denir. Bu tür denklemler genellikle konikleri (elips, hiperbol, parabol) temsil eder. Birden fazla denklemden oluşan sisteme ise ikinci dereceden iki bilinmeyenli denklem sistemi denir. Çözüm kümesi, sistemdeki tüm denklemleri sağlayan $(x, y)$ gerçek sayı ikililerinden oluşur. Çözüm bulunurken yerine koyma veya yok etme metotları kullanılır. Geometrik olarak, çözüm kümesi denklemlerin grafiklerinin kesişim noktalarına karşılık gelir. Örneğin, $x^2 + y^2 - xy - 16 = 0$ ile $x^2 + y = 9$ denklemlerinin grafikleri dört noktada kesişiyorsa, çözüm kümesi dört elemanlıdır. Bu, iki koniğin kesişim noktalarının sayısının en fazla dört olabileceği gerçeğini yansıtır.

# İkinci Dereceden Denklem ve Eşitsizlik Sistemleri

İşaret tablosu, polinom eşitsizliklerini çözmek için sistematik bir yol sunar. Tek katlı köklerde işaret değişir, çift katlı köklerde değişmez. Çözüm kümesine dahil etme durumuna göre semboller kullanılır. İkinci dereceden bir bilinmeyenli eşitsizliklerin işaret incelemesi, $ax^2 + bx + c = 0$ denkleminin diskriminantına göre yapılır. Eğer $\Delta > 0$ ise, $x$ eksenini iki noktada kesen parabol söz konusudur. Kökler arasında $a$ ile zıt işaretli, kökler dışında $a$ ile aynı işaretli olur. Bu, ikinci dereceden bir fonksiyonun kökler arasında işaret değiştirmesinden kaynaklanır. Eğer $\Delta = 0$ ise, $x$ eksenine teğet parabol vardır. Her yerde $a$ ile aynı işaretlidir (teğet noktasında sıfır). Çift kat köklerde işaret değişmez. Eğer $\Delta < 0$ ise, $x$ eksenini kesmeyen parabol vardır. Her yerde $a$ ile aynı işaretlidir. Bu durumda parabol ya tamamen pozitif ya da tamamen negatiftir. Eşitsizliklerin çözüm kümesi, $f(x) = ax^2 + bx + c$ için $f(x) > 0$, $f(x) \ge 0$, $f(x) < 0$, $f(x) \le 0$ gibi ifadelerin sağlandığı $x$ değerleridir. Eğer her $x \in \mathbb{R}$ için $ax^2 + bx + c > 0$ ise $a > 0$ ve $\Delta < 0$ olmalıdır. Eğer her $x \in \mathbb{R}$ için $ax^2 + bx + c < 0$ ise $a < 0$ ve $\Delta < 0$ olmalıdır. Bu koşullar, parabolün tamamen pozitif veya tamamen negatif olması için gereklidir.

# İki İfadenin Çarpımı veya Bölümü Şeklinde Verilen Eşitsizliklerin Çözüm Kümesi

$f(x) \cdot g(x) \ge 0$ (veya $\le 0$) ya da $\frac{f(x)}{g(x)} \ge 0$ (veya $\le 0$) şeklindeki eşitsizliklerin çözümü için şu adımlar izlenir. İlk olarak, $f(x) = 0$ ve $g(x) = 0$ denklemlerinin kökleri bulunur ve sayı doğrusuna yerleştirilir. Ardından, $f(x)$ ve $g(x)$ polinomlarının en büyük dereceli terimlerinin katsayılarının işaretleri çarpılır. Bu işaret, tablonun en sağındaki aralığın işaretidir. Bunun nedeni, $x$ çok büyük pozitif değerler alırken polinomların en büyük dereceli terimlerinin baskın olmasıdır. Her aralıkta işaret belirlenirken, tek katlı köklerde işaret değişir, çift katlı köklerde değişmez. Bölüm şeklindeki eşitsizliklerde, paydayı sıfır yapan kökler çözüm kümesine asla dâhil edilmez (payda sıfır olamaz). Payı sıfır yapan kökler ise $\ge$ veya $\le$ durumunda dâhil edilebilir. Örneğin, $(x+3)(x^2+x-2) \le 0$ eşitsizliğinin çözüm kümesi $(-\infty, -3] \cup [-2, 1]$ olur. Bu yöntem, rasyonel eşitsizliklerin çözümünde standarttır.

# İkinci Dereceden Bir Bilinmeyenli Eşitsizlik Sistemi

İki veya daha fazla eşitsizliğin bir araya gelmesiyle oluşan sisteme eşitsizlik sistemi denir. Sistemdeki tüm eşitsizlikleri aynı anda sağlayan değerlerin kümesine çözüm kümesi denir. İkinci dereceden bir bilinmeyenli eşitsizlik sistemlerinde, eşitsizliklerden en az biri ikinci derecedendir. Çözüm bulmak için her bir eşitsizliğin çözüm aralığı ayrı ayrı bulunur, ardından bu aralıkların kesişimi alınır. Ortak işaret tablosu oluşturmak bu işlemi kolaylaştırır. Örneğin, $\begin{cases} x^2 + 3x - 4 \ge 0 \\ x^2 - 2x - 3 \le 0 \end{cases}$ sisteminin çözüm kümesi $[1, 3]$ olur. Bu, her iki eşitsizliği de sağlayan $x$ değerlerinin birleşimidir.

# Koşullu Olasılık

$E$ eş olasılıklı bir örnek uzay olsun. $A$ ve $B$ iki olay olsun. $B$ olayının gerçekleştiği bilindiği durumda $A$ olayının gerçekleşme olasılığına $A$ olayının $B$ olayına bağlı koşullu olasılığı denir ve $P(A \mid B)$ ile gösterilir. $P(B) > 0$ olmak koşuluyla:
\[
P(A \mid B) = \frac{P(A \cap B)}{P(B)}.
\]
Bu formülün mantığı, $B$'nin gerçekleştiğini bildiğimizde, örnek uzayı $B$ ile sınırlandırmamız ve $A$'nın bu yeni örnek uzay içindeki olasılığını hesaplamamızdır. Bu eşitlikten $P(A \cap B) = P(B) \cdot P(A \mid B)$ çarpma kuralı elde edilir. Eğer örnek uzayın tüm sonuçları eş olasılıklı ise, koşullu olasılık şu şekilde de hesaplanabilir:
\[
P(A \mid B) = \frac{s(A \cap B)}{s(B)},
\]
yani $A$ ve $B$'nin kesişimindeki eleman sayısının $B$'nin eleman sayısına oranı. Örneğin, bir grupta 10 kız ve 8 erkek 10. sınıf, 6 kız ve 14 erkek 11. sınıf olsun. Rastgele seçilen bir öğrencinin erkek olduğu bilindiğine göre 10. sınıf olma olasılığı $\frac{8}{22} = \frac{4}{11}$ olur. Burada, erkek öğrencilerin sayısı 22 olduğu için örnek uzay bu 22 kişiye indirgenir; bunlardan 8'i 10. sınıftır.

# Bağımsız Olaylar

$A$ ve $B$ iki olay olsun. Eğer $A$ olayının gerçekleşmesi $B$ olayının gerçekleşme olasılığını etkilemiyorsa (veya tersi), bu olaylara bağımsız olaylar denir. Bağımsızlık durumunda $P(A \mid B) = P(A)$ olur. Koşullu olasılık tanımından $P(A \cap B) = P(A) \cdot P(B)$ elde edilir. Bu, bağımsızlığın temel karakterizasyonudur. Eğer $P(A \cap B) \neq P(A)P(B)$ ise olaylar bağımlı olarak adlandırılır. $A$ veya $B$'nin gerçekleşme olasılığı ise $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ ile hesaplanır. Ayrıca, $P(A \text{ ya da } B) = P(A \cap B') + P(B \cap A')$ şeklinde de ifade edilebilir. Bu, sadece birinin gerçekleştiği durumu temsil eder.

# Bileşik Olayların Olasılığı

Birden fazla basit olaydan oluşan olaylara bileşik olay denir. Bileşik olaylarda iki veya daha çok olay birlikte ya da birbiri ardınca gerçekleşir. Örneğin, bir zarı arka arkaya iki kez attığımızda ilk atışta asal sayı, ikinci atışta çift sayı gelmesi bir bileşik olaydır. Ayrıca, bir torbadan top çekip başka bir torbaya atma ve ardından ikinci torbadan top çekme gibi ardışık işlemler de bileşik olaylardır. Bileşik olayların olasılığını hesaplamak için ağaç diyagramı kullanmak oldukça pratiktir. Ağaç diyagramı, tüm olasılık yollarını görselleştirir ve her bir dalın olasılığını çarparak toplam olasılığı bulmayı sağlar. Örneğin, A torbasında 4 yeşil 5 mavi, B torbasında 6 yeşil 3 mavi, C torbasında 2 yeşil 4 mavi top olsun. A'dan rastgele bir top çekilir; yeşilse B'den, maviyse C'den bir top çekilir. Çekilen topun yeşil olma olasılığı:
\[
\frac{4}{9} \cdot \frac{6}{9} + \frac{5}{9} \cdot \frac{2}{6} = \frac{8}{27} + \frac{5}{27} = \frac{13}{27}.
\]
Burada ilk terim, A'dan yeşil çekme ve ardından B'den yeşil çekme olasılığını; ikinci terim, A'dan mavi çekme ve ardından C'den yeşil çekme olasılığını temsil eder.

# Deneysel Olasılık

Deneysel olasılık, bir olayın gerçekleşme sıklığının toplam deney sayısına oranıdır. Teorik olasılık ise olayın olası tüm sonuçlar içindeki matematiksel oranıdır. Deneysel olasılık, deney sayısı arttıkça teorik olasılığa yaklaşır. Bu, büyük sayılar yasası olarak bilinir ve rastgele olayların uzun vadede istikrarlı bir oran sergilediğini ifade eder. Örneğin, bir madeni parayı 100 kez atıp 48 tura gelmesi durumunda tura gelme deneysel olasılığı 0,48 iken teorik olasılık 0,5'tir. Atış sayısı arttıkça deneysel olasılık 0,5'e yaklaşır. Deneysel olasılık, özellikle teorik modelin karmaşık olduğu veya bilinmediği durumlarda kullanışlıdır. Örneğin, bir ürünün hatalı çıkma olasılığını belirlemek için testler yapılır.

# Yönlü Açılar

Kenarlarından biri başlangıç, diğeri bitiş kenarı olarak belirlenmiş açıya yönlü açı denir. Yönlü açılarda sıra önemlidir; $\widehat{AOB}$ ile $\widehat{BOA}$ farklı açılardır. Saat yönünün tersi yöndeki dönüş pozitif yön, saat yönündeki dönüş ise negatif yön olarak kabul edilir. Bu yönlendirme, trigonometride ve dönme hareketlerinde standarttır. Örneğin, bir cismin dönme açısı pozitif veya negatif olarak ifade edilir. Derece, açı ölçmek için yaygın bir birimdir. Bir çemberin çevresinin 360 eşit parçaya ayrılmasıyla elde edilen her bir parçaya karşılık gelen merkez açıya 1 derecelik açı denir ve $1^\circ$ ile gösterilir. 360 sayısının kullanılmasının tarihsel nedenleri arasında, eski uygarlıkların yılı yaklaşık 360 gün olarak alması ve 360'ın çok sayıda böleni olması yer alır. Daha küçük birimler: 1 derecenin $\frac{1}{60}$'ine 1 dakika ($1'$) denir, $1^\circ = 60'$. 1 dakikanın $\frac{1}{60}$'ına 1 saniye ($1''$) denir, $1' = 60''$. Bu altmışlık sistem, Babil matematiğinden gelir. Radyan, matematiksel analizde daha doğal bir birimdir. Bir çemberin yarıçap uzunluğundaki yayı gören merkez açının ölçüsüne 1 radyan denir. Radyan kullanmanın avantajı, trigonometrik fonksiyonların türev ve integral formüllerini basitleştirmesidir. Derece ve radyan arasındaki dönüşüm: $\frac{D}{180} = \frac{R}{\pi}$, burada $D$ derece, $R$ radyan cinsinden ölçüdür. Bu oran, tam çemberin 360° veya $2\pi$ radyan olmasından gelir. Bir açının esas ölçüsü, onun $[0^\circ, 360^\circ)$ veya $[0, 2\pi)$ aralığındaki karşılığıdır. Yani $k \in \mathbb{Z}$ olmak üzere $\alpha + k \cdot 360^\circ$ açısının esas ölçüsü $\alpha$ derecedir (benzer şekilde radyan için $\alpha + k \cdot 2\pi$). Esas ölçü, periyodik fonksiyonlarda değerleri karşılaştırmayı kolaylaştırır. Saatin dönme yönü negatif, tersi pozitiftir.

# Birim Çember

Analitik düzlemde merkezi orijin $O(0,0)$ ve yarıçapı 1 birim olan çembere birim çember denir. Birim çember üzerindeki herhangi bir $P(x, y)$ noktası $x^2 + y^2 = 1$ denklemini sağlar. Örneğin, $P\left(\frac{1}{\sqrt{2}}, a\right)$ noktası birim çember üzerinde ise $\left(\frac{1}{\sqrt{2}}\right)^2 + a^2 = 1 \Rightarrow a^2 = \frac{1}{2} \Rightarrow a = \pm \frac{1}{\sqrt{2}}$ olur. Bu iki değerin çarpımı $-\frac{1}{2}$'dir. Birim çember, trigonometrik fonksiyonların tanımlanmasında temel rol oynar. Birim çember sayesinde trigonometrik fonksiyonlar sadece dik üçgenle sınırlı kalmayıp tüm gerçek sayılarda tanımlanabilir. Ayrıca, birim çember üzerinde açıların radyan cinsinden ölçülmesi doğaldır.

# Sinüs ve Kosinüs Fonksiyonları

Birim çember üzerinde $P(\cos \alpha, \sin \alpha)$ noktasını ele alalım. Burada $\alpha$, $OP$ doğrusunun $x$ ekseni ile pozitif yönde yaptığı açıdır. Bir dik üçgende karşı dik kenarın hipotenüse oranı sinüs, komşu dik kenarın hipotenüse oranı kosinüs olduğundan, birim çemberde hipotenüs 1 olduğu için doğrudan $\sin \alpha = y$ ve $\cos \alpha = x$ olur. Bu tanım, açıların derece veya radyan cinsinden her değeri için geçerlidir. Buradan $\cos^2 \alpha + \sin^2 \alpha = 1$ özdeşliği elde edilir. Sinüs ve kosinüs fonksiyonlarının tanım kümeleri $\mathbb{R}$, görüntü kümeleri ise $[-1, 1]$'dir. Yani her $\alpha$ için $-1 \le \sin \alpha \le 1$ ve $-1 \le \cos \alpha \le 1$ olur. Bu sınırlar, birim çember üzerindeki noktaların koordinatlarının mutlak değerinin 1'i geçememesinden kaynaklanır. Sinüs ve kosinüs, periyodik fonksiyonların en temel örnekleridir ve periyotları $2\pi$'dir.

# Tanjant ve Kotanjant Fonksiyonları

Birim çemberde $x$ ekseni ile pozitif yönde $\alpha$ açısı yapan $[OP$ ışınının, $x=1$ doğrusu (tanjant ekseni) ile kesiştiği nokta $B(1, \tan \alpha)$ olur. Bu nedenle $\tan \alpha = \frac{\sin \alpha}{\cos \alpha}$ olarak tanımlanır. Tanjant fonksiyonunun tanım kümesi $\cos \alpha \neq 0$ olan açılardır, yani $\alpha \neq \frac{\pi}{2} + k\pi$. Bu durumlarda $\cos \alpha = 0$ olduğu için tanjant tanımsızdır. Görüntü kümesi $\mathbb{R}$'dir. Benzer şekilde, $y=1$ doğrusu (kotanjant ekseni) ile kesişim noktası $C(\cot \alpha, 1)$ olup $\cot \alpha = \frac{\cos \alpha}{\sin \alpha}$ ve $\tan \alpha \cdot \cot \alpha = 1$'dir. Kotanjantın tanım kümesi $\sin \alpha \neq 0$, yani $\alpha \neq k\pi$; görüntü kümesi $\mathbb{R}$'dir. Tanjant ve kotanjant fonksiyonlarının periyodu $\pi$'dir.

# Sekant ve Kosekant Fonksiyonu

Sekant ve kosekant, sırasıyla kosinüs ve sinüsün çarpmaya göre tersi olarak tanımlanır:
\[
\sec \alpha = \frac{1}{\cos \alpha}, \qquad \csc \alpha = \frac{1}{\sin \alpha}.
\]
Sekant fonksiyonunun tanım kümesi $\cos \alpha \neq 0$ yani $\alpha \neq \frac{\pi}{2} + k\pi$, görüntü kümesi $\mathbb{R} \setminus (-1, 1)$'dir. Çünkü $|\cos \alpha| \le 1$ olduğundan $|\sec \alpha| \ge 1$ olur. Kosekant için tanım kümesi $\sin \alpha \neq 0$ yani $\alpha \neq k\pi$, görüntü kümesi de $\mathbb{R} \setminus (-1, 1)$'dir. Bu fonksiyonlar, trigonometrik denklemlerde ve bazı integrallerde kullanılır. Ayrıca, bazı geometrik problemlerde, birim çembere teğet doğruların uzunlukları olarak yorumlanabilirler.

# Bir Açının Trigonometrik Değerlerinin Dar Açı Cinsinden Yazılması

Herhangi bir açının trigonometrik değerleri, esas ölçüsü bulunarak ve uygun indirgeme formülleri kullanılarak dar açı cinsinden ifade edilebilir. İndirgeme kuralları şöyledir. $\pi \pm \alpha$ veya $2\pi \pm \alpha$ şeklindeki açılarda: İlk önce açının bulunduğu bölgeye göre trigonometrik fonksiyonun işareti belirlenir, ardından fonksiyon değiştirilmeden $\alpha$'nın trigonometrik değeri yazılır. Bu kural, bu açıların birim çember üzerinde $\alpha$'nın yatay veya dikey yansıması olmasından gelir. $\frac{\pi}{2} \pm \alpha$ veya $\frac{3\pi}{2} \pm \alpha$ şeklindeki açılarda: Yine işaret belirlenir, ancak bu kez fonksiyon değişir: $\sin \leftrightarrow \cos$, $\tan \leftrightarrow \cot$, $\sec \leftrightarrow \csc$. Bu değişim, bu açıların birim çember üzerinde dik eksenlere göre yansımasından kaynaklanır. Örneğin, $\sin(\pi + \alpha) = -\sin \alpha$ (III. bölgede sinüs negatif, fonksiyon değişmez). $\cos\left(\frac{\pi}{2} - \alpha\right) = \sin \alpha$ (I. bölgede kosinüs pozitif, fonksiyon değişir).

# Trigonometrik Fonksiyonların İşaretleri

Birim çemberde açının bulunduğu bölgeye göre trigonometrik fonksiyonların işaretleri aşağıdaki gibidir. Bu kuralı hatırlamak için "ASTC" veya "All Students Take Calculus" ifadesi kullanılır. I. bölge ($0 < \alpha < \frac{\pi}{2}$): Tüm fonksiyonlar pozitif. II. bölge ($\frac{\pi}{2} < \alpha < \pi$): Sadece $\sin$ (ve onun tersi $\csc$) pozitif; $\cos$, $\tan$, $\cot$, $\sec$ negatif. III. bölge ($\pi < \alpha < \frac{3\pi}{2}$): Sadece $\tan$ ve $\cot$ pozitif; diğerleri negatif. IV. bölge ($\frac{3\pi}{2} < \alpha < 2\pi$): Sadece $\cos$ ve $\sec$ pozitif; diğerleri negatif. Bu işaretler, trigonometrik denklemlerin çözümünde ve ifadelerin sadeleştirilmesinde kritik öneme sahiptir. Örneğin, bir denklemin çözümünü bulurken hangi bölgede olduğunu bilmek, hangi köklerin geçerli olduğunu belirlemeyi sağlar.

# Kosinüs Teoremi

Herhangi bir $ABC$ üçgeninde kenar uzunlukları $a = |BC|$, $b = |AC|$, $c = |AB|$ ve karşı açılar sırasıyla $\widehat{A}$, $\widehat{B}$, $\widehat{C}$ olmak üzere kosinüs teoremi şu bağıntıları verir:
\[
a^2 = b^2 + c^2 - 2bc \cos \widehat{A}, \quad
b^2 = a^2 + c^2 - 2ac \cos \widehat{B}, \quad
c^2 = a^2 + b^2 - 2ab \cos \widehat{C}.
\]
Teorem, Pisagor teoreminin genelleştirilmiş halidir. Dik üçgende $\cos 90^\circ = 0$ olduğundan $a^2 = b^2 + c^2$ elde edilir. Kosinüs teoremi, iki kenar ve aralarındaki açı bilindiğinde üçüncü kenarı bulmak veya üç kenar bilindiğinde açıları hesaplamak için kullanılır. Örneğin, $\cos \widehat{A} = \frac{b^2 + c^2 - a^2}{2bc}$ şeklinde de yazılabilir. Bu formül, bir üçgenin açısını hesaplamada doğrudan kullanışlıdır. Ayrıca, kosinüs teoremi vektörlerin skaler çarpımı ile de ilişkilidir.

# Sinüs Teoremi

Bir $ABC$ üçgeninde kenar uzunlukları ile karşı açıların sinüsleri arasında şu ilişki vardır:
\[
\frac{a}{\sin \widehat{A}} = \frac{b}{\sin \widehat{B}} = \frac{c}{\sin \widehat{C}} = 2R,
\]
burada $R$ üçgenin çevrel çemberinin yarıçapıdır. Sinüs teoremi, bir kenar ve karşısındaki açı ile başka bir açı bilindiğinde diğer kenarı bulmak için kullanılır. Ayrıca, üçgenin alanı $A = \frac{1}{2}bc \sin \widehat{A} = \frac{1}{2}ac \sin \widehat{B} = \frac{1}{2}ab \sin \widehat{C}$ şeklinde de hesaplanabilir. Teoremin ispatı, bir kenara ait yüksekliğin iki farklı şekilde ifade edilmesiyle yapılır: $h = b \sin \widehat{C} = c \sin \widehat{B}$ gibi. Sinüs teoremi, özellikle çevrel çember ile ilgili problemlerde ve üçgenin kenarları ile açıları arasında dönüşüm yaparken kullanılır.

# Periyot ve Periyodik Fonksiyonlar

Bir $f(x)$ fonksiyonunun tanım kümesindeki her $x$ için $f(x+T) = f(x)$ eşitliğini sağlayan pozitif bir $T$ sayısı varsa, $f$ fonksiyonuna periyodik fonksiyon, en küçük böyle $T$ sayısına da periyot denir. Trigonometrik fonksiyonlar periyodiktir. $\sin x$ ve $\cos x$ için periyot $2\pi$'dir: $\sin(x + 2\pi k) = \sin x$, $\cos(x + 2\pi k) = \cos x$. Bunun nedeni, birim çember üzerinde $2\pi$ radyanlık bir dönüşün aynı noktaya geri dönmesidir. $\tan x$ ve $\cot x$ için periyot $\pi$'dir: $\tan(x + \pi k) = \tan x$, $\cot(x + \pi k) = \cot x$. Bu, tanjant ve kotanjantın birim çember üzerinde $\pi$ radyan sonra aynı değeri almasından kaynaklanır (çünkü $\tan(\alpha + \pi) = \tan \alpha$). Daha genel olarak, $a \neq 0$ olmak üzere $\sin(ax + b) + c$ ve $\cos(ax + b) + c$ fonksiyonlarının periyodu $\frac{2\pi}{|a|}$; $\tan(ax + b) + c$ ve $\cot(ax + b) + c$ fonksiyonlarının periyodu ise $\frac{\pi}{|a|}$'dir. Bu, $x$'in katsayısının periyodu ters orantılı olarak etkilediğini gösterir.

# Trigonometrik Fonksiyonların Grafikleri

Sinüs fonksiyonu $f(x) = \sin x$, periyot $2\pi$, tanım kümesi $\mathbb{R}$, görüntü kümesi $[-1,1]$. Grafik orijinden geçer, $x = \frac{\pi}{2}$'de maksimum 1, $x = \frac{3\pi}{2}$'de minimum -1, $x = 0, \pi, 2\pi$'de sıfırdır. Sinüs grafiği, birim çemberdeki y-koordinatının açıya göre değişimini temsil eder. Kosinüs fonksiyonu $f(x) = \cos x$, periyot $2\pi$, görüntü $[-1,1]$. $x=0$'da maksimum 1, $x=\pi$'de minimum -1, $x = \frac{\pi}{2}, \frac{3\pi}{2}$'de sıfırdır. Grafik, sinüs grafiğinin $\frac{\pi}{2}$ sola ötelenmiş halidir: $\cos x = \sin(x + \frac{\pi}{2})$. Tanjant fonksiyonu $f(x) = \tan x$, periyot $\pi$, tanım kümesi $x \neq \frac{\pi}{2} + k\pi$, görüntü $\mathbb{R}$. Düşey asimptotları $x = \frac{\pi}{2} + k\pi$'dir. $x=0$'da sıfır, $x = \frac{\pi}{4}$'te 1, $x = -\frac{\pi}{4}$'te -1'dir. Artan bir fonksiyondur. Tanjant grafiği, birim çemberdeki tanjant ekseninin değişimini gösterir. Kotanjant fonksiyonu $f(x) = \cot x$, periyot $\pi$, tanım kümesi $x \neq k\pi$, görüntü $\mathbb{R}$. Düşey asimptotları $x = k\pi$'dir. Azalan bir fonksiyondur. Kotanjant, tanjantın çarpmaya göre tersi olduğu için grafikleri birbirinin yatay yansıması gibidir.

# Ters Trigonometrik Fonksiyonlar

Trigonometrik fonksiyonlar birebir olmadıkları için terslerini tanımlamak üzere tanım kümeleri kısıtlanır. Bu kısıtlama, her bir fonksiyonun birebir ve örten olduğu bir aralık seçilerek yapılır. Arksinüs: $\arcsin x$: $[-1,1] \to [-\frac{\pi}{2}, \frac{\pi}{2}]$, $\arcsin x = y \iff \sin y = x$. Bu aralıkta sinüs birebirdir ve değer kümesi $[-1,1]$'dir. Arkkosinüs: $\arccos x$: $[-1,1] \to [0, \pi]$, $\arccos x = y \iff \cos y = x$. $[0,\pi]$ aralığında kosinüs birebirdir. Arktanjant: $\arctan x$: $\mathbb{R} \to (-\frac{\pi}{2}, \frac{\pi}{2})$, $\arctan x = y \iff \tan y = x$. Bu aralıkta tanjant birebirdir ve tüm reel değerleri alır. Arkkotanjant: $\operatorname{arccot} x$: $\mathbb{R} \to (0, \pi)$, $\operatorname{arccot} x = y \iff \cot y = x$. Bu fonksiyonlar, trigonometrik denklemlerin çözüm kümelerini ifade etmede kullanılır. Örneğin, $\sin x = a$ denkleminin çözümü $x = \arcsin a + 2k\pi$ veya $x = \pi - \arcsin a + 2k\pi$ şeklindedir.

# Sinüs ve Kosinüs Fonksiyonlarının Toplam-Fark Formülleri

Toplam-fark formülleri, iki açının toplamının veya farkının trigonometrik değerlerini, açıların ayrı ayrı trigonometrik değerleri cinsinden verir. Bu formüller, trigonometrik özdeşliklerin temelini oluşturur.
\[
\cos(\alpha + \beta) = \cos\alpha \cos\beta - \sin\alpha \sin\beta, \qquad
\cos(\alpha - \beta) = \cos\alpha \cos\beta + \sin\alpha \sin\beta.
\]
\[
\sin(\alpha + \beta) = \sin\alpha \cos\beta + \cos\alpha \sin\beta, \qquad
\sin(\alpha - \beta) = \sin\alpha \cos\beta - \cos\alpha \sin\beta.
\]
Bu formüller, kosinüs teoreminin ispatında ve diğer trigonometrik özdeşliklerin türetilmesinde temel rol oynar. Ayrıca, karmaşık sayıların kutupsal gösteriminde ($e^{i\theta} = \cos\theta + i\sin\theta$) ve dalga mekaniğinde sıklıkla kullanılır. Örneğin, iki dalganın üst üste binmesi bu formüllerle analiz edilir.

# Tanjant ve Kotanjant Fonksiyonlarının Toplam-Fark Formülleri

Tanjant ve kotanjant için toplam-fark formülleri sinüs ve kosinüs formüllerinden türetilir:
\[
\tan(\alpha + \beta) = \frac{\tan\alpha + \tan\beta}{1 - \tan\alpha \tan\beta}, \qquad
\tan(\alpha - \beta) = \frac{\tan\alpha - \tan\beta}{1 + \tan\alpha \tan\beta}.
\]
\[
\cot(\alpha + \beta) = \frac{\cot\alpha \cot\beta - 1}{\cot\alpha + \cot\beta}, \qquad
\cot(\alpha - \beta) = \frac{\cot\alpha \cot\beta + 1}{\cot\beta - \cot\alpha}.
\]
Bu formüller, özellikle $\tan$ veya $\cot$ içeren denklemlerin çözümünde ve integrallerde faydalıdır. Ayrıca, bazı trigonometrik limitlerin hesaplanmasında da kullanılırlar.

# Sinüs ve Kosinüs Fonksiyonlarının İki Kat Açı Formülleri

Toplam formüllerinde $\beta = \alpha$ alınarak iki kat açı formülleri elde edilir:
\[
\sin 2\alpha = 2 \sin\alpha \cos\alpha.
\]
\[
\cos 2\alpha = \cos^2\alpha - \sin^2\alpha = 1 - 2\sin^2\alpha = 2\cos^2\alpha - 1.
\]
Bu eşitliklerden ayrıca:
\[
(\sin\alpha + \cos\alpha)^2 = 1 + \sin 2\alpha, \quad (\sin\alpha - \cos\alpha)^2 = 1 - \sin 2\alpha.
\]
Kosinüs iki kat açı formülü, açılım yapılarak çarpanlarına ayrılabilir:
\[
\cos 2\alpha = (\cos\alpha - \sin\alpha)(\cos\alpha + \sin\alpha) = (1 - \sqrt{2}\sin\alpha)(1 + \sqrt{2}\sin\alpha) = (\sqrt{2}\cos\alpha - 1)(\sqrt{2}\cos\alpha + 1).
\]
Bu formüller, trigonometrik denklemleri çözmede ve integralleri sadeleştirmede kullanılır.

# Tanjant ve Kotanjant Fonksiyonlarının İki Kat Açı Formülleri

Tanjant ve kotanjant için iki kat açı formülleri:
\[
\tan 2\alpha = \frac{2\tan\alpha}{1 - \tan^2\alpha}, \qquad
\cot 2\alpha = \frac{\cot^2\alpha - 1}{2\cot\alpha}.
\]
Bu formüller, trigonometrik denklemleri çözerken veya belirli integralleri hesaplarken kullanılır. Ayrıca, $\tan 2\alpha$ ifadesi $\frac{2\tan\alpha}{(1-\tan\alpha)(1+\tan\alpha)}$ şeklinde de yazılabilir. Bu yazım, bazı denklemlerde çarpanlara ayırmayı kolaylaştırır.

# Sinx = a, Cosx = a, Tanx = a ve Cotx = a Denklemlerinin Çözüm Kümesi

İçinde bilinmeyenin trigonometrik fonksiyonları bulunan denklemlere trigonometrik denklem denir. Temel trigonometrik denklemlerin çözüm kümeleri, periyodiklik ve ters fonksiyonlar kullanılarak bulunur. $\sin x = a$ ($a \in [-1,1]$) için birim çemberde sinüs değeri $a$ olan iki nokta vardır (x ve $\pi - x$). Bu nedenle çözüm: $x = \arcsin a + 2k\pi$ veya $x = \pi - \arcsin a + 2k\pi$, $k \in \mathbb{Z}$. $\cos x = a$ ($a \in [-1,1]$) için: $x = \arccos a + 2k\pi$ veya $x = -\arccos a + 2k\pi$, $k \in \mathbb{Z}$. $\tan x = a$ ($a \in \mathbb{R}$) için tanjantın periyodu $\pi$ olduğundan $x = \arctan a + k\pi$, $k \in \mathbb{Z}$. $\cot x = a$ ($a \in \mathbb{R}$) için: $x = \operatorname{arccot} a + k\pi$, $k \in \mathbb{Z}$. Bu çözümler, periyodiklik dikkate alınarak genelleştirilmiştir.

# Sinx ve Cosx'e Göre Lineer (Doğrusal) ve Homojen Denklemlerin Çözüm Kümesi

Lineer denklemler $a \sin x + b \cos x = c$ biçimindedir. Çözmek için eşitliğin her iki tarafı $\sqrt{a^2+b^2}$'ye bölünür ve bir $\phi$ açısı $\cos\phi = \frac{a}{\sqrt{a^2+b^2}}$, $\sin\phi = \frac{b}{\sqrt{a^2+b^2}}$ olacak şekilde seçilirse denklem $\sin(x+\phi) = \frac{c}{\sqrt{a^2+b^2}}$ haline gelir. Bu dönüşümün mantığı, $a$ ve $b$'nin bir dik üçgenin kenarları olarak düşünülmesidir. Bu denklemin çözümü için $\left|\frac{c}{\sqrt{a^2+b^2}}\right| \le 1$ olmalıdır. Aksi halde çözüm yoktur. Homojen denklemler $a \sin x + b \cos x = 0$ biçimindedir. $\cos x \neq 0$ olduğu durumda her iki taraf $\cos x$'e bölünerek $a \tan x + b = 0$ yani $\tan x = -\frac{b}{a}$ elde edilir. Bu da standart tanjant denklemidir. $\cos x = 0$ durumu ayrıca kontrol edilmelidir; bu durumda $\sin x = \pm 1$ olur ve denklemin sağlanması için $a \cdot (\pm 1) = 0$ yani $a=0$ olması gerekir, bu da denklemin homojen olma özelliğini bozar.

# Üstel ve Logaritmik Fonksiyonlar

Üstel fonksiyon: $a \in \mathbb{R}^+ \setminus \{1\}$ olmak üzere $f: \mathbb{R} \to \mathbb{R}^+$, $f(x) = a^x$ şeklinde tanımlanır. Taban pozitif ve 1'den farklı olmalıdır. Tabanın 1 olması durumunda sabit fonksiyon elde edilir, tersi tanımlanamaz. $a>1$ ise $f$ artan, $0<a<1$ ise azalandır. Her zaman $f(0)=1$ olduğundan grafik $y$ eksenini $(0,1)$'de keser. Üstel fonksiyon birebir ve örten olduğu için tersi vardır; bu ters logaritma fonksiyonudur. Logaritma fonksiyonu: $f(x) = a^x$'in tersi $f^{-1}(x) = \log_a x$ olarak tanımlanır. $y = a^x \iff x = \log_a y$. Tanım kümesi $\mathbb{R}^+$, görüntü kümesi $\mathbb{R}$'dir. $a>1$ iken $\log_a x$ artan, $0<a<1$ iken azalandır. $\log_a 1 = 0$, $\log_a a = 1$. Logaritmanın özellikleri, üstel fonksiyonların özelliklerinden türetilir ($a^{x+y}=a^x a^y$ vb.):
1. $\log_a(xy) = \log_a x + \log_a y$
2. $\log_a\left(\frac{x}{y}\right) = \log_a x - \log_a y$
3. $\log_a(x^n) = n \log_a x$
4. Taban değiştirme: $\log_a b = \frac{\log_c b}{\log_c a}$ (özellikle $\log_a b = \frac{1}{\log_b a}$)
5. $a^{\log_b c} = c^{\log_b a}$

Doğal logaritma: Tabanı $e \approx 2.71828$ olan logaritmaya denir ve $\ln x$ ile gösterilir. $e$, Euler sayısı olarak bilinir ve $e = \sum_{n=0}^{\infty} \frac{1}{n!}$ şeklinde tanımlanır. Doğal logaritma, matematiksel analizde en yaygın kullanılan logaritmadır çünkü türevi $\frac{d}{dx} \ln x = \frac{1}{x}$ basittir. Üstel ve logaritmik denklemler: Üstel denklemlerde genellikle her iki tarafın aynı tabanda logaritması alınır. Logaritmik denklemlerde tanım koşullarına ($\log_a f(x)$ için $f(x)>0$, $a>0$, $a\neq1$) dikkat edilir. Üstel ve logaritmik eşitsizlikler: $a>1$ için $a^{f(x)} \ge a^{g(x)} \iff f(x) \ge g(x)$; $0<a<1$ için yön değiştirir. Logaritmik eşitsizliklerde de benzer şekilde tabanın 1'den büyük veya küçük olmasına göre yön değişir. Ayrıca logaritmanın tanımından $f(x)>0$ ve $g(x)>0$ olmalıdır.

# Gerçek Hayat Durumları İle İlgili Üstel ve Logaritmik Fonksiyon Problemleri

Üstel ve logaritmik fonksiyonlar, doğada ve bilimde sıkça karşılaşılan büyüme ve bozunma süreçlerini modellemek için kullanılır. Ses şiddeti desibel cinsinden $L = 10 \log\left(\frac{I}{I_0}\right)$ formülüyle hesaplanır; $I$ ses şiddeti, $I_0 = 10^{-12}$ W/m² işitme eşiğidir. Logaritma kullanılmasının nedeni, insan kulağının ses şiddetindeki değişimleri logaritmik olarak algılamasıdır. Richter ölçeğine göre deprem büyüklüğü $R = \log d$ ile verilir; $d$ mikron cinsinden maksimum genliktir. Richter ölçeği de logaritmiktir çünkü deprem dalgalarının genliği çok geniş bir aralıkta değişir. Karbon-14 yaş tayini: $N(t) = N_0 \left(\frac{1}{2}\right)^{t/5730}$ veya $t = -5730 \frac{\ln(N/N_0)}{\ln 2}$; 5730 yıl yarılanma süresidir. Radyoaktif bozunma üstel bir süreçtir. Bu modeller sayesinde fosillerin yaşı, depremin büyüklüğü ve sesin şiddeti gibi nicelikler hesaplanabilir.

# Dizi Kavramı ve Dizinin Terimleri

$A$ ve $B$ boş olmayan iki küme olmak üzere, $A$'nın her elemanını $B$'nin bir ve yalnız bir elemanına eşleyen ilişkiye fonksiyon denir. Özel olarak, $\mathbb{Z}^+$ (pozitif tam sayılar) kümesinden $\mathbb{R}$'ye tanımlanan her fonksiyona gerçek sayı dizisi veya kısaca dizi denir. $f(n) = a_n$ olmak üzere, dizi $(a_n)$ ile gösterilir. $a_n$ değerine dizinin $n.$ terimi veya genel terimi adı verilir. Genel terimi verilmeyen bir sayı kümesi dizi belirtmez çünkü bir dizi, tanımı gereği her $n$ için bir kural belirtmelidir. Dizi, $(a_n) = (a_1, a_2, a_3, \dots)$ şeklinde yazılır.

# Dizi Çeşitleri ve İndirgeme Bağıntısı

$A = \{1,2,\dots, r\} \subset \mathbb{Z}^+$ için $A \to \mathbb{R}$'ye tanımlanan dizilere sonlu dizi denir. Belirtilmediği sürece diziler sonsuz kabul edilir. Genel terimi sabit olan $(a_n) = (c, c, c, \dots)$ dizisine sabit dizi denir. İki dizi, her $n$ için $a_n = b_n$ ise eşittir. Bir dizinin terimi, kendinden önceki bir veya birkaç terim cinsinden tanımlanıyorsa buna indirgemeli dizi, tanımlama bağıntısına da indirgeme bağıntısı denir. İndirgemeli diziler, özellikle bilgisayar bilimlerinde ve kombinatoryal problemlerde sıkça kullanılır. Örneğin, üçgensel sayılar: $1, 3, 6, 10, 15, \dots$ genel terimi $a_n = \frac{n(n+1)}{2}$ olan sayılardır. Ardışık iki üçgensel sayının toplamı bir karesel sayıdır: $\frac{(n-1)n}{2} + \frac{n(n+1)}{2} = n^2$. Bu, geometrik bir yorumla da görülebilir: üçgen şeklinde dizilmiş noktaların yan yana konması kare oluşturur.

# Aritmetik Dizi ve Özellikleri

Ardışık terimleri arasındaki farkın sabit olduğu diziye aritmetik dizi denir. Yani $a_{n+1} - a_n = d$ (ortak fark). Bu sabit fark, dizinin doğrusal bir şekilde değiştiğini gösterir. Genel terim: $a_n = a_1 + (n-1)d$. Sonlu bir aritmetik dizide baştan ve sondan eşit uzaklıktaki terimlerin toplamı eşittir: $a_1 + a_n = a_2 + a_{n-1} = \dots$. Bu özellik, terimlerin simetrik dağılımından gelir. Ayrıca $a_k$ ve $a_p$ biliniyorsa $d = \frac{a_p - a_k}{p-k}$. İki sayı $a$ ve $b$ arasına $p$ tane terim yerleştirilerek aritmetik dizi oluşturulursa ortak fark $d = \frac{b-a}{p+1}$ olur. Aritmetik dizide bir terim, kendisine eşit uzaklıktaki iki terimin aritmetik ortalamasıdır: $a_n = \frac{a_{n-k} + a_{n+k}}{2}$.

# Geometrik Dizi ve Özellikleri

Ardışık terimleri arasındaki oranın sabit olduğu diziye geometrik dizi denir: $\frac{a_{n+1}}{a_n} = r$ (ortak çarpan). Bu sabit oran, dizinin üstel bir şekilde değiştiğini gösterir. Genel terim: $a_n = a_1 \cdot r^{n-1}$. Ayrıca $a_n = a_k \cdot r^{n-k}$. Sonlu geometrik dizide baştan ve sondan eşit uzaklıktaki terimlerin çarpımı eşittir: $a_1 \cdot a_n = a_2 \cdot a_{n-1} = \dots$. Bu, aritmetik dizideki toplam özelliğinin çarpımsal analogudur. Geometrik dizide bir terim, kendisine eşit uzaklıktaki iki terimin geometrik ortalamasıdır: $a_n = \sqrt{a_{n-k} \cdot a_{n+k}}$. Ortak çarpan $r = \sqrt[k-p]{\frac{a_k}{a_p}}$ ile bulunur. İki sayı $a$ ve $b$ arasına $k$ terim yerleştirilerek geometrik dizi oluşturulursa $r = \sqrt[k+1]{\frac{b}{a}}$ olur.

# Aritmetik ve Geometrik Dizide İlk N Terim Toplamları

Sigma gösterimi $\sum_{k=1}^{n} a_k = a_1 + a_2 + \dots + a_n$, toplamları kısa ve öz bir şekilde ifade etmeyi sağlar. Bir aritmetik dizinin ilk $n$ terim toplamı $S_n = \frac{n}{2}(a_1 + a_n) = \frac{n}{2}(2a_1 + (n-1)d)$ olarak hesaplanır. Bu formül, Gauss'un meşhur 1'den 100'e kadar olan sayıları toplama yönteminin genelleştirilmesidir: terimleri çiftler halinde toplamak. Bir geometrik dizinin ilk $n$ terim toplamı ($r \neq 1$) $S_n = a_1 \frac{1 - r^n}{1 - r}$ formülüyle bulunur. ($r=1$ durumunda $S_n = n a_1$). Bu formül, $(1-r)S_n = a_1(1-r^n)$ eşitliğinden türetilir. Geometrik diziler, özellikle finans (bileşik faiz) ve bilgisayar bilimlerinde (algoritma analizi) sıkça kullanılır.

# Gerçek Hayat Durumları İle İlgili Dizi Problemleri

Fibonacci dizisi: $1, 1, 2, 3, 5, 8, 13, 21, \dots$ şeklinde ilerler. İlk iki terim 1, sonraki her terim kendinden önceki iki terimin toplamıdır: $a_1=1$, $a_2=1$, $a_n = a_{n-1} + a_{n-2}$ ($n>2$). Genel terimi $a_n = \frac{1}{\sqrt{5}}\left[\left(\frac{1+\sqrt{5}}{2}\right)^n - \left(\frac{1-\sqrt{5}}{2}\right)^n\right]$ olan Fibonacci dizisi, doğada (örneğin ayçiçeği tohumları, sarmal kabuklar) ve finansal piyasalarda sıkça görülür. Ünlü tavşan problemi: Bir çift tavşan her ay yeni bir çift doğurur (iki ay sonra cinsel olgunluğa ulaşarak). Başlangıçta bir çift ile başlandığında aylık tavşan sayıları Fibonacci dizisini verir. Bu problem, popülasyon dinamiklerinin basit bir modelidir.

# Limit ve Süreklilik

Yaklaşım kavramı: $x$ değişkeni $a$'ya $a$'dan küçük değerlerle yaklaşıyorsa soldan yaklaşım ($x \to a^-$), $a$'dan büyük değerlerle yaklaşıyorsa sağdan yaklaşım ($x \to a^+$) denir. Bir $f(x)$ fonksiyonunun $x=a$ noktasındaki soldan limiti $\lim_{x\to a^-} f(x) = L_1$, sağdan limiti $\lim_{x\to a^+} f(x) = L_2$ olarak tanımlanır. Eğer $L_1 = L_2 = L$ ise $\lim_{x\to a} f(x) = L$ vardır; aksi halde limit yoktur. Limit varlığı için fonksiyonun $a$'da tanımlı olması gerekmez. Grafikte kopukluk olan noktalara kritik nokta denir. Limit, bir fonksiyonun bir nokta civarındaki davranışını tanımlar. Limit ile ilgili özellikler, limitin doğrusal bir operatör olduğunu gösterir. Sabit fonksiyonun limiti sabittir. Polinomlarda $\lim_{x\to x_0} f(x) = f(x_0)$ (süreklilik). Toplam, fark, çarpım, bölüm (payda sıfır değilse) limitleri ayrı ayrı alınabilir. $k$ sabit için $\lim k f(x) = k \lim f(x)$. $\lim [f(x)]^n = [\lim f(x)]^n$ (uygun koşullarda). Köklü ifadelerde, $n$ tek veya çift koşullarına dikkat edilerek limit içeriye taşınabilir. Mutlak değer, üstel ve logaritmik fonksiyonlarda da limit içeriye taşınabilir. Trigonometrik fonksiyonlarda $\lim_{x\to a} \sin x = \sin a$, $\lim_{x\to a} \cos x = \cos a$, vb. (tanım kümelerine dikkat). Parçalı tanımlı fonksiyonların limiti: Kritik nokta dışında o noktanın ait olduğu parça kullanılır. Kritik noktada soldan ve sağdan limitler ayrı ayrı hesaplanır. Limitte belirsizlik durumları: $\frac{0}{0}$ belirsizliğinde pay ve payda çarpanlarına ayrılıp sadeleştirme yapılır. Rasyonel fonksiyonlarda ortak çarpan sadeleştirildiğinde, sadeleşen nokta dışında grafik aynıdır; limit hesaplaması sadeleştirilmiş fonksiyonla yapılabilir. L'Hospital kuralı: $\frac{0}{0}$ veya $\frac{\infty}{\infty}$ belirsizliklerinde $\lim \frac{f(x)}{g(x)} = \lim \frac{f'(x)}{g'(x)}$ (türevler alınarak) belirsizlik giderilene kadar uygulanabilir. Bu kural, Cauchy'nin ortalama değer teoreminin bir sonucudur. Süreklilik: $f$ fonksiyonu $x=a$'da süreklidir ancak ve ancak $\lim_{x\to a} f(x) = f(a)$. Soldan ve sağdan süreklilik benzer şekilde tanımlanır. Polinomlar her yerde süreklidir. Rasyonel fonksiyonlar paydanın sıfır olduğu noktalar dışında süreklidir. Süreklilik, türevin varlığı için gerekli ancak yeterli değildir.

# Türev

Anlık değişim oranı (türev): $f$ fonksiyonunun $x=a$ noktasındaki türevi
\[
f'(a) = \lim_{x\to a} \frac{f(x)-f(a)}{x-a} = \lim_{h\to 0} \frac{f(a+h)-f(a)}{h}
\]
olarak tanımlanır. Türev, geometrik olarak fonksiyonun $x=a$ noktasındaki teğetinin eğimidir. Fizikte bir hareketlinin anlık hızını verir. Bu limitin varlığı, fonksiyonun o noktada türevlenebilir olduğu anlamına gelir. Soldan ve sağdan türev: $f'(a^-) = \lim_{x\to a^-} \frac{f(x)-f(a)}{x-a}$, $f'(a^+) = \lim_{x\to a^+} \frac{f(x)-f(a)}{x-a}$. Eğer $f$ $x=a$'da sürekli ve $f'(a^-) = f'(a^+)$ ise $f'(a)$ vardır. Türevli olmak sürekliliği gerektirir, ancak sürekli bir fonksiyon türevli olmayabilir (örneğin $f(x)=|x|$ $x=0$'da türevsizdir). Kırılma noktalarında soldan ve sağdan türevler farklıdır.

# Türev Alma Kuralları

Sabit fonksiyon: $f(x)=c \Rightarrow f'(x)=0$. Sabit bir fonksiyonun değişim hızı sıfırdır. Kuvvet kuralı: $f(x)=ax^n \Rightarrow f'(x)=a n x^{n-1}$ ($n$ rasyonel). Bu kural, binom teoremi ve limit tanımı kullanılarak türetilir. İkinci türev: $f''(x) = \frac{d^2 f}{dx^2}$, türevin türevi olup ivme veya eğrilik gibi kavramlarla ilişkilidir. Toplam/fark: $(f \pm g)' = f' \pm g'$. Çarpım: $(f \cdot g)' = f' g + g' f$. Bu, türevin limit tanımından gelir. Bölüm: $\left(\frac{f}{g}\right)' = \frac{f' g - g' f}{g^2}$ ($g \neq 0$). Zincir kuralı: $(f \circ g)'(x) = f'(g(x)) \cdot g'(x)$. Özel olarak $\frac{d}{dx} [f(x)]^n = n [f(x)]^{n-1} f'(x)$.

# Türevlenebilen İki Fonksiyonun Toplamının, Farkının, Çarpımının ve Bölümünün Türevi

Bu kurallar yukarıda verilmiştir. Pratikte, çarpım ve bölüm türevlerinin formüllerini doğru hatırlamak önemlidir. Çarpım kuralı "birincinin türevi çarpı ikinci artı ikincinin türevi çarpı birinci" şeklinde söylenebilir. Bölüm kuralı ise "(payın türevi çarpı payda eksi paydanın türevi çarpı pay) bölü paydanın karesi" şeklinde.

# İki Fonksiyonun Bileşkesinin Türevi

Zincir kuralı, bileşke fonksiyonların türevini hesaplamak için temel araçtır. Örneğin, $y = \sin(x^2)$ ise $y' = \cos(x^2) \cdot 2x$. $y = \sqrt{1+x^2}$ ise $y' = \frac{1}{2\sqrt{1+x^2}} \cdot 2x = \frac{x}{\sqrt{1+x^2}}$. Zincir kuralı, dış fonksiyonun türevi ile iç fonksiyonun türevinin çarpımıdır.

# Bir Fonksiyonun Artan ve Azalan Olduğu Aralıklar

$f$ $[a,b]$'de sürekli ve $(a,b)$'de türevlenebilir olsun. Her $x \in (a,b)$ için $f'(x) > 0$ ise $f$ $[a,b]$'de artandır. Her $x \in (a,b)$ için $f'(x) < 0$ ise $f$ $[a,b]$'de azalandır. $f'(x) = 0$ ise $f$ sabittir. Bu bilgi, bir fonksiyonun grafiğini çizerken hangi aralıklarda yükseldiğini veya alçaldığını belirlemeye yarar. Türevin işareti, fonksiyonun eğimini gösterir.

# Bir Fonksiyonun Ekstremum Noktaları

Yerel maksimum: Bir $x_0$ noktasının bir komşuluğundaki tüm $x$ için $f(x) \le f(x_0)$ ise $(x_0, f(x_0))$ yerel maksimum noktasıdır. Yerel minimum: $f(x) \ge f(x_0)$ ise yerel minimum noktasıdır. Mutlak maksimum/minimum: Tanım kümesinin tamamında en büyük/en küçük değer. Eğer $f$, $x_0$'da türevlenebilir ve bir ekstremum noktası ise $f'(x_0) = 0$ olur. Bu, Fermat teoremidir. Teoremin mantığı, eğer türev pozitif olsaydı sağ tarafta daha büyük değerler, negatif olsaydı sol tarafta daha büyük değerler olacağı için ekstremum olamazdı. Ancak $f'(x_0)=0$ olması ekstremum için yeterli değildir (örneğin $f(x)=x^3$'te $x=0$). Türev olmayan noktalarda da ekstremum olabilir (örneğin $f(x)=|x|$'te $x=0$). Ekstremum noktalarını bulmak için $f'(x)=0$ denkleminin kökleri ve türevsizlik noktaları incelenir.

# Türev Yardımıyla Bir Fonksiyonun Grafiğinin Çizimi

Bir fonksiyonun grafiğini çizmek için şu adımlar izlenir: Tanım kümesini belirle. Eksenleri kestiği noktaları bul ($f(x)=0$, $f(0)$). Türevi kullanarak artan/azalan aralıkları ve ekstremum noktalarını bul. İkinci türevle (varsa) konvekslik/konkavlık ve dönüm noktalarını belirle. İkinci türev pozitifse fonksiyon konveks (yukarı bükük), negatifse konkav (aşağı bükük). Asimptotları (düşey, yatay, eğik) araştır. Bu bilgileri kullanarak grafiği çiz. Doğrunun eğimi $m = \tan \alpha$ veya $m = -\frac{a}{b}$ ($ax+by+c=0$ için). İki noktası bilinen doğrunun eğimi $m = \frac{y_2-y_1}{x_2-x_1}$. Paralel doğruların eğimleri eşit, dik doğruların eğimleri çarpımı $-1$'dir.

# Maksimum Minimum Problemleri

Optimizasyon problemlerinde, maksimize veya minimize edilmek istenen nicelik tek bir değişkene bağlı bir fonksiyon olarak ifade edilir. Daha sonra bu fonksiyonun türevi alınarak kritik noktalar bulunur ve bu noktalarda fonksiyonun değeri hesaplanır. Ayrıca tanım aralığının uç noktaları da kontrol edilir. İkinci dereceden bir fonksiyon $f(x)=ax^2+bx+c$ için tepe noktası $x=-\frac{b}{2a}$'da olup $f$'nin maksimum veya minimum değeri $k = \frac{4ac-b^2}{4a}$'dır. Türev yöntemiyle de $f'(x)=2ax+b=0$'dan aynı nokta bulunur. Türev, ekonomi (kar maksimizasyonu, maliyet minimizasyonu), fizik, mühendislik ve veri analizinde yaygın olarak kullanılır.

# Belirsiz İntegral

$F'(x) = f(x)$ ise $F(x)$'e $f(x)$'in ters türevi veya belirsiz integrali denir ve $\int f(x) dx = F(x) + c$ ile gösterilir, $c$ integral sabitidir. Belirsiz integral, türevin ters işlemidir ve bir fonksiyonun tüm ters türevlerini (bir sabit farkıyla) verir. Temel integral kuralları: $\int x^n dx = \frac{x^{n+1}}{n+1} + c$ ($n \neq -1$). ($n=-1$ durumunda $\int x^{-1} dx = \ln|x| + c$.) $\int af(x) dx = a \int f(x) dx$. $\int [f(x) \pm g(x)] dx = \int f(x) dx \pm \int g(x) dx$.

# Diferansiyel Kavramı ve Değişken Değiştirme (İkame) Yöntemi

Diferansiyel: $d(f(x)) = f'(x) dx$. Diferansiyel, küçük değişimleri ifade eder ve integral alma işleminde değişken değiştirme için kullanılır. Değişken değiştirme (ikame) yöntemi: $\int f(x)^n f'(x) dx$ tipindeki integrallerde $u = f(x)$, $du = f'(x) dx$ dönüşümü yapılarak $\int u^n du = \frac{u^{n+1}}{n+1} + c$ elde edilir. Bu yöntem, zincir kuralının tersine uygulanmasıdır. Benzer şekilde $\int \frac{f'(x)}{[f(x)]^n} dx$ için $u = f(x)$ dönüşümü ile $\int u^{-n} du$ bulunur. $\int f'(g(x)) g'(x) dx$ tipinde ise $u = g(x)$ dönüşümü ile $\int f'(u) du = f(u) + c$ olur. Değişken değiştirme, karmaşık integralleri basitleştirmek için güçlü bir tekniktir.

# Riemann Toplamı

$[a,b]$ aralığının $P = \{x_0, x_1, \dots, x_n\}$ bölüntüsü (genellikle eşit aralıklı $\Delta x = \frac{b-a}{n}$) ve her alt aralıktan seçilen $c_i \in [x_{i-1}, x_i]$ için $\sum_{i=1}^n f(c_i) \Delta x$ toplamına Riemann toplamı denir. Eğer $c_i$ alt aralıktaki en küçük değer ise Riemann alt toplamı, en büyük değer ise Riemann üst toplamı olur. $n \to \infty$ iken Riemann toplamı, eğrinin altındaki alana yaklaşır ve bu limit değeri belirli integral olarak tanımlanır: $\lim_{n\to\infty} \sum_{i=1}^n f(c_i) \Delta x = \int_a^b f(x) dx$. Riemann toplamı, integralin tanımını oluşturur ve sayısal integral hesaplamalarının temelidir.

# Belirli İntegral

$f$ $[a,b]$'de sürekli ve $F'(x)=f(x)$ ise $\int_a^b f(x) dx = F(b) - F(a)$. Bu, Newton-Leibniz teoremi olarak bilinir. Belirli integral, $f$'nin $[a,b]$ aralığında $x$ ekseni ile arasındaki net alanı (üstteki alan eksi alttaki alan) verir. İntegral sabiti $c$ sadeleşir.

# Belirli İntegralin Özellikleri

$\int_a^a f(x) dx = 0$ (noktanın alanı sıfırdır). $\int_a^b f(x) dx = -\int_b^a f(x) dx$ (yön değiştirince işaret değişir). $\int_a^b f(x) dx = \int_a^c f(x) dx + \int_c^b f(x) dx$ ($a<c<b$) (alanların toplanabilirliği). $\int_a^b k f(x) dx = k \int_a^b f(x) dx$ (skaler çarpma). $\int_a^b [f(x) \pm g(x)] dx = \int_a^b f(x) dx \pm \int_a^b g(x) dx$ (lineerlik). Parçalı tanımlı fonksiyonlarda integral, parçaların ayrı ayrı integrali alınarak toplanır.

# Belirli İntegral İle Alan Hesaplama

$y=f(x)$ grafiği, $x=a$, $x=b$ ve $x$ ekseni arasında kalan bölgenin alanı $A = \int_a^b |f(x)| dx$ ile hesaplanır. Eğer $f(x) \ge 0$ ise $A = \int_a^b f(x) dx$; $f(x) \le 0$ ise $A = -\int_a^b f(x) dx$. $f$ işaret değiştiriyorsa, integral pozitif ve negatif kısımlara ayrılır. $\int_a^b f(x) dx$ ifadesi net alanı verirken, $\int_a^b |f(x)| dx$ toplam alanı verir.

# İki Fonksiyon Grafiği Arasında Kalan Sınırlı Bölgenin Alanı

$[a,b]$ aralığında $f(x) \ge g(x)$ ise iki eğri arasındaki alan $A = \int_a^b [f(x) - g(x)] dx$. Eğer sıralama değişiyorsa, alan sıralamanın değiştiği noktalara göre parçalara ayrılarak mutlak değer içinde integral alınır: $A = \int_a^b |f(x) - g(x)| dx$.

# Analitik Düzlem

İki sayı doğrusunun $O$ noktasında bir yatay bir dikey olarak dik kesişmesiyle oluşan sisteme dik koordinat sistemi, bu sistemin bulunduğu düzleme analitik düzlem denir. Yatay eksen $x$ ekseni (apsis ekseni), dikey eksen $y$ ekseni (ordinat ekseni). Bir $A(a,b)$ noktasının koordinatları, $x=a$ ve $y=b$ doğrularının kesiştiği noktadır. Orijin $O(0,0)$'dır. Eksenler düzlemi dört bölgeye ayırır: I. bölge $x>0, y>0$; II. bölge $x<0, y>0$; III. bölge $x<0, y<0$; IV. bölge $x>0, y<0$.

# Analitik Geometri

İki nokta arası uzaklık: $A(x_1,y_1)$, $B(x_2,y_2)$ için $|AB| = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$. Bu, Pisagor teoreminin doğrudan uygulamasıdır. İçten bölen nokta: $A(x_1,y_1)$, $B(x_2,y_2)$ için $\frac{|AC|}{|BC|} = k$ olan $C$ noktası $C\left(\frac{x_1 + kx_2}{1+k}, \frac{y_1 + ky_2}{1+k}\right)$. Bu formül, benzer üçgenlerden türetilir. Dıştan bölen nokta: $C\left(\frac{x_1 - kx_2}{1-k}, \frac{y_1 - ky_2}{1-k}\right)$. Orta nokta: $k=1$ alınarak $C\left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$. Paralelkenarda köşegenlerin orta noktaları aynı olduğundan $x_1 + x_3 = x_2 + x_4$, $y_1 + y_3 = y_2 + y_4$. Üçgenin ağırlık merkezi: $G\left(\frac{x_1+x_2+x_3}{3}, \frac{y_1+y_2+y_3}{3}\right)$. Ağırlık merkezi, kenarortayların kesiştiği noktadır. Doğrunun eğimi: $m = \tan \alpha = \frac{y_2-y_1}{x_2-x_1}$. $y=mx+n$'de eğim $m$, $ax+by+c=0$'da $m=-\frac{a}{b}$. Doğru denklemleri: Eğimi $m$, $A(x_1,y_1)$'den geçen: $y-y_1 = m(x-x_1)$. İki noktası bilinen: $\frac{y-y_1}{x-x_1} = \frac{y_2-y_1}{x_2-x_1}$. Eksen kesişimleri $(a,0)$ ve $(0,b)$: $\frac{x}{a} + \frac{y}{b} = 1$. $x$ eksenine paralel: $y = b$; $y$ eksenine paralel: $x = a$. Orijinden geçen: $y = mx$. İki doğrunun durumu: Çakışık: $\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}$. Paralel: $\frac{a_1}{a_2} = \frac{b_1}{b_2} \neq \frac{c_1}{c_2}$. Kesişen: $\frac{a_1}{a_2} \neq \frac{b_1}{b_2}$. Dik: $m_1 m_2 = -1$. Bir noktanın doğruya uzaklığı: $h = \frac{|ax_1+by_1+c|}{\sqrt{a^2+b^2}}$. Bu formül, noktadan doğruya dikme indirilerek ve alan yöntemiyle türetilir. Paralel iki doğru arası uzaklık: $h = \frac{|c_1 - c_2|}{\sqrt{a^2+b^2}}$.

# Dönüşümler

Öteleme: $A(x,y)$ noktası $x$ ekseni boyunca $a$ birim sağa: $A'(x+a, y)$; sola: $A'(x-a, y)$. $y$ ekseni boyunca $a$ birim yukarı: $A'(x, y+a)$; aşağı: $A'(x, y-a)$. Öteleme, şeklin yerini değiştirir, şekli bozmaz. Dönme: Orijin etrafında pozitif yönde $\alpha$ dönme: $R_\alpha(x,y) = (x\cos\alpha - y\sin\alpha, x\sin\alpha + y\cos\alpha)$. Bu, dönme matrisi ile ifade edilir. Özel durumlar: $R_{90^\circ}(x,y)=(-y,x)$, $R_{180^\circ}(x,y)=(-x,-y)$, $R_{270^\circ}(x,y)=(y,-x)$, $R_{360^\circ}(x,y)=(x,y)$. Simetri: Bir noktaya göre: $A(x,y)$'nin $B(a,b)$'ye göre simetriği $(2a-x, 2b-y)$. Orijine göre: $(-x,-y)$. $x$ eksenine göre: $(x,-y)$. $y$ eksenine göre: $(-x,y)$. $y=x$ doğrusuna göre: $(y,x)$. Bir doğruya göre: Diklik ve orta nokta koşulları kullanılır. Ötelemeli dönme ve ötelemeli simetri: Şekillerin uzunlukları korunur, açıların yönü değişebilir. Bu dönüşümler, kristalografide ve süsleme sanatlarında kullanılır.

# Çember ve Daire

Çember: Bir düzlemde sabit bir noktadan (merkez) eşit uzaklıkta (yarıçap) bulunan noktaların kümesi. Kiriş: Uçları çember üzerinde olan doğru parçası. Çap: merkezden geçen kiriş, $|AB|=2r$. Teğet: Çembere bir noktada değen doğru. Teğet, değme noktasında yarıçapa diktir. Yay: Çember üzerindeki iki nokta arasındaki parça. Merkez açı: Köşesi merkezde, ölçüsü gördüğü yayın ölçüsüne eşit. Çevre açı: Köşesi çember üzerinde, ölçüsü gördüğü yayın yarısına eşit. Thales teoremi: çapı gören çevre açı diktir. Teğet-kiriş açı: Köşesi çember üzerinde, bir kolu teğet diğeri kiriş. Ölçüsü gördüğü yayın yarısı. İç açı: Çemberin içinde kesişen iki kirişin oluşturduğu açı. Ölçüsü, gördüğü yayların toplamının yarısı. Dış açı: Çemberin dışındaki bir noktadan çizilen iki kesen/teğetin oluşturduğu açı. Ölçüsü, gördüğü yayların farkının yarısı. Çevrel çember: Üçgenin köşelerinden geçen çember. Sinüs teoremi: $\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R$. İç teğet çember: Üçgenin üç kenarına teğet olan çember. Merkezi iç açıortayların kesişimi. Yarıçapı $r = \frac{2\Delta}{a+b+c}$ ($\Delta$ alan). Dış teğet çember: Bir kenara ve diğer iki kenarın uzantılarına teğet. Dairenin çevresi: $2\pi r$. $\pi$ sayısı, tüm çemberlerde çevrenin çapa oranı sabitidir. Dairenin alanı: $\pi r^2$. Daire diliminin çevresi: $2r + \frac{\alpha}{360^\circ} \cdot 2\pi r$. Daire diliminin alanı: $\frac{\alpha}{360^\circ} \cdot \pi r^2$.

# Çemberin Standart Denklemi

Merkezi $M(a,b)$, yarıçapı $r$ olan çemberin denklemi: $(x-a)^2 + (y-b)^2 = r^2$. Bu, iki nokta arası uzaklık formülünün doğrudan uygulamasıdır. Özel durumlar: Merkez orijin: $x^2 + y^2 = r^2$. $x$ ekseni üzerinde: $(x-a)^2 + y^2 = r^2$. $y$ ekseni üzerinde: $x^2 + (y-b)^2 = r^2$. $y$ eksenine teğet: $(x-a)^2 + (y-b)^2 = a^2$. $x$ eksenine teğet: $(x-a)^2 + (y-b)^2 = b^2$. Her iki eksene teğet: $(x \mp r)^2 + (y \mp r)^2 = r^2$ (bölgeye göre işaretler).

# Çemberin Analitik İncelenmesi

Genel denklem: $x^2 + y^2 + Dx + Ey + F = 0$. Merkez $M\left(-\frac{D}{2}, -\frac{E}{2}\right)$, yarıçap $r = \frac{1}{2}\sqrt{D^2+E^2-4F}$. $D^2+E^2-4F > 0$ ise çember, $=0$ ise nokta, $<0$ ise sanal çember. $Ax^2 + By^2 + Cxy + Dx + Ey + F = 0$ denkleminin çember belirtmesi için $A = B \neq 0$, $C=0$ ve $D^2+E^2-4AF > 0$ (uygun düzenleme ile).

# Çember İle Doğrunun Birbirine Göre Durumları

Merkezin doğruya uzaklığı $h$ ile yarıçap $r$ karşılaştırılır: $h < r$ ise iki kesim noktası, $h = r$ ise teğet, $h > r$ ise kesmez. Cebirsel olarak, doğru denklemi çember denkleminde yerine yazılıp elde edilen ikinci derece denklemin diskriminantına bakılır: $\Delta > 0$ iki kesim, $\Delta = 0$ teğet, $\Delta < 0$ kesmez.

# Dik Dairesel Silindirde Uzunluk ve Alan

Dik dairesel silindir, tabanları birbirine eşit daireler ve yanal yüzeyi dikdörtgen olan bir cisimdir. Taban yarıçapı $r$, yükseklik $h$ olan böyle bir silindirin yanal alanı $Y_A = 2\pi r h$ olarak hesaplanır; çünkü yan yüzey, yüksekliği $h$ ve genişliği taban çevresi $2\pi r$ olan bir dikdörtgendir. Taban alanı $T_A = \pi r^2$ olduğundan, silindirin toplam yüzey alanı $S_A = 2\pi r h + 2\pi r^2$ formülüyle bulunur.

# Silindirin Hacmi

Dik dairesel silindirin hacmi, taban alanı ile yüksekliğin çarpımıdır: $V = \pi r^2 h$. Bu, prizmalar için geçerli olan "taban alanı çarpı yükseklik" kuralının bir örneğidir.

# Dik Dairesel Konide Uzunluk ve Alan

Dik dairesel koni, tepe noktasından taban merkezine inen dikmeyle simetrik bir konidir. Taban yarıçapı $r$, yükseklik $h$ ve ana doğru uzunluğu $l = \sqrt{r^2 + h^2}$ (Pisagor teoremi) olan bir koninin yanal yüzeyi, bir daire dilimi şeklinde açılır. Bu daire diliminin yarıçapı $l$ ve yay uzunluğu taban çevresi $2\pi r$ olduğu için yanal alan, daire diliminin alanı formülünden $Y_A = \pi r l$ olarak elde edilir. Taban alanı $\pi r^2$ olduğuna göre, koninin toplam yüzey alanı $A = \pi r l + \pi r^2$ ile hesaplanır.

# Dik Dairesel Konide Hacim

Koninin hacmi, aynı taban ve yüksekliğe sahip silindirin hacminin üçte biridir: $V = \frac{1}{3} \pi r^2 h$. Bu, piramitler için geçerli olan "taban alanı çarpı yükseklik bölü 3" kuralının bir örneğidir. Arşimet, bu oranı keşfetmiştir.

# Kürede Uzunluk, Alan ve Hacim

Küre, merkezden eşit uzaklıktaki noktaların oluşturduğu yüzeydir. Yarıçapı $r$ olan bir kürenin yüzey alanı $4\pi r^2$, hacmi ise $\frac{4}{3}\pi r^3$ tür. Bir kürenin bir düzlemle arakesiti bir çemberdir. Bu çember kürenin merkezinden geçiyorsa büyük çember adını alır ve yarıçapı $r$'dir. Kürenin yüzey alanı, büyük çember alanının 4 katıdır. Hacim formülü, integral hesabıyla veya Arşimet'in yöntemiyle türetilebilir.