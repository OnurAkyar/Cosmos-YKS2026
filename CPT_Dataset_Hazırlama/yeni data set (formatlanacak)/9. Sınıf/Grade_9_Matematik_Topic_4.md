# **MATEMATİK Sınıf-9**

![](_page_0_Picture_1.jpeg)

## KONU KÜMELERDE İŞLEMLER-II

## FARK İŞLEMİ VE BİR KÜMENİN TÜMLEYENİ

#### KÜMELERDE FARK İŞLEMİ

A ve B birer küme olmak üzere A kümesinde olup B kümesinde olmayan tüm elemanların oluşturduğu kümeyi A kümesinin B kümesinden farkı denir.  $A\!-\!B$  veya  $A\setminus B$  ile gösterilir.

$$A-B=\{x \mid x \in A \text{ ve } x \notin B\}$$

$$B-A=\{x \mid x \in B \text{ ve } x \notin A\}$$

#### KÜMELERDE FARK İŞLEMİNİN ÖZELLİKLERİ

1) Fark işleminin değişme özelliği yoktur.

$$A \neq B$$
 iken  $B - A \neq A - B$ 

2) Bir kümenin kendisinden farkı boş kümedir.

$$A-A=\phi$$

- 3) Bir A kümesinin evrensel kümeden farkı boş kümedir.  $A-E=\phi$
- 4) Bir A kümesinin boş kümden farkı kendisidir.  $A \phi = A$

#### **AYRIK KÜMELER**

A ve B birer küme olmak üzere  $A \cap B = \phi$  ise

A ile B ayrık kümelerdir.

A ve B ayrık kümeler olmak üzere A-B=A ve B-A=B olur.

#### **BİR KÜMENİN TÜMLEYENİ**

E evrensel küme,  $A \subset E$  olmak üzere evrensel kümede olup A kümesinde olmayan elemanların kümesine A kümesinin tümleyeni denir. A'ile gösterilir.

$$A' = \{x \mid x \notin A \text{ ve } x \in E\}$$

![](_page_0_Picture_21.jpeg)

A kümesi ile A' kümesinin eleman esit olur. s(A) + s(A') = s(E)

A kümesi ile A kümesinin eleman sayılarının toplamı evrensel kümenin eleman sayısına esit olur. s(A) + s(A') = s(E)

#### TÜMLEYEN İŞLEMİNİN ÖZELLİKLERİ

- $\rightarrow$  (A')' = A
- $\triangleright$   $\phi' = E$ ,  $E' = \phi$
- $\rightarrow$   $A \subset B \Rightarrow B' \subset A'$
- $\rightarrow$  A $\cup$ A'=E, A $\cap$ A'= $\phi$
- $\triangleright$  E $\cup$ A'=E, E $\cap$ A'=A'
- $\rightarrow$  A-B = A $\cap$ B', B-A = B $\cap$ A'

#### **DE MORGAN KURALLARI**

- $\rightarrow$   $(A \cup B)' = A' \cap B'$
- $(A \cap B)' = A' \cup B'$

### KÜMELER İLE SEMBOLİK MANTIK KURALLARI ARASINDAKİ İLİŞKİ

| Sei | mbolik mantık ile<br>gösterimi | 0 | 1 | ٨ | V | Değili (')   | Ξ |
|-----|--------------------------------|---|---|---|---|--------------|---|
| Ki  | üme işlemleri ile<br>gösterimi | Ø | Е | 0 | U | Tümleyeni(') | - |

| Sembolik Mantık İle                                         | Kümeler İle                                      |  |  |  |
|-------------------------------------------------------------|--------------------------------------------------|--|--|--|
| (p′)′ <u>=</u> p                                            | (A')' = A                                        |  |  |  |
| $p\wedge p'\equiv 0$                                        | A∩A′=∅                                           |  |  |  |
| 1 ∧ 0 ≡ 0                                                   | Enø=ø                                            |  |  |  |
| $p \vee p' \equiv 1$                                        | A∪A' = E                                         |  |  |  |
| $p \wedge (q \vee r) \equiv (p \wedge q) \vee (p \wedge r)$ | $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ |  |  |  |
| $(p \wedge q)' \equiv p' \vee q'$                           | $(A \cap B)' = A' \cup B'$                       |  |  |  |

#### **SORULAR**

**SORU 1:** A ve B, E evrensel kümesinin iki alt kümesi olmak üzere

$$3.s(A \setminus B) = 6.s(A \cap B) = 2.s(B \cap A')$$
 ve  $s(A \cup B) = 42$  ise  $s(A)$  nin değeri kaçtır?

- A) 7 B) 14
  - C) 21
- D) 23
- E) 25 Cevap C

**SORU 2:** A, B ve C kümeleri aynı evrensel kümenin alt kümeleri olmak üzere

$$s(A) + s(B') = 8+2x$$
,  $s(B) + s(C) = 10-x$   
 $s(C') + s(A') = 12 - x$  ve  $s(C) = 4$  ise  $s(C')$  kactir?

- A) 4 B)
  - B) 6
- C) 10
- D)12 E) 18
  - Cevap B

**SORU 3:** 24 kişilik bir sınıfta kimya veya fizik derslerinden geçenler ile kalanlar vardır. Kimya veya fizik derslerinden kalanların sayısı 4,yalnız bir dersten geçen 12 kişi ise her iki dersten geçen kaç kişi vardır?

- A) 8
- B)10
- C) 11
- D) 12
- E) 14

Cevap A