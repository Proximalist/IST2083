# IST2083 — Temel İstatistik ve R ile Veri Analizi

**Marmara Üniversitesi, Siyasal Bilgiler Fakültesi · 2026–2027 Güz**
Prof. Dr. Hakan Mehmetcik · Perşembe 14:00–17:00 · RTE.S1.138

Bu depo dersin tüm materyallerini barındırır: ders notları, sunumlar,
alıştırmalar, cevap anahtarları ve veri setleri.

---

## Hızlı başlangıç

Derse hiç R kurmadan başlıyorsanız sırayla:

1. **[R ve RStudio Kurulum Rehberi](R_RStudio_Kurulum_Rehberi.qmd)** — R,
   RStudio, Git ve gerekli paketlerin kurulumu.
2. **[GitHub Kullanım Kılavuzu](GitHub_Kullanim_Kilavuzu.qmd)** — bu deponun
   bilgisayarınıza indirilmesi ve **her hafta güncellenmesi.**
3. **[Ders İzlencesi](izlence/IST2083-izlence-2026-2027-guz.qmd)** — konular,
   tarihler, değerlendirme ve kaynaklar.
4. **[R Hızlı Referans](R-Hizli-Referans.qmd)** — dönem boyunca öğrenilen
   R sözdizimini tek yerde toplayan, her hafta büyüyen başvuru belgesi.
   Bir sözdizimini unuttuğunuzda önce buraya bakın.

Bilgisayarınıza hiçbir şey kurmak istemiyorsanız GitHub Codespaces
seçeneği de vardır; kılavuzda anlatılmıştır.

---

## Ders programı

| # | Tarih | Konu | Klasör |
|---:|---|---|---|
| 1 | 1 Ekim | Giriş: istatistiğin anlamı; R, RStudio, GitHub | `01_hafta/` |
| 2 | 8 Ekim | R'da veri türleri, veri yapıları ve temel fonksiyonlar | `02_hafta/` |
| — | 15 Ekim | *Ders yapılmaz* | — |
| 3 | 22 Ekim | Veri işleme: `dplyr`, `tidyr`; Quarto ile raporlama | `05_hafta/`, `06_hafta/` |
| — | 29 Ekim | *Cumhuriyet Bayramı* | — |
| 4 | 5 Kasım | Veri görselleştirme: `ggplot2` | `03_hafta/` |
| 5 | 12 Kasım | Tanımlayıcı istatistik | `04_hafta/` |
| — | 19 Kasım | **ARA SINAV** — kapsam: 1.–5. oturumlar | — |
| 6 | 26 Kasım | Olasılık, rastgele değişkenler ve dağılımlar | `06_hafta/`, `08_hafta/` |
| 7 | 3 Aralık | Örnekleme ve Merkezi Limit Teoremi | `07_hafta/` |
| T | *Telafi* | Tahmin ve güven aralıkları | `09_hafta/` |
| 8 | 10 Aralık | Hipotez testi I: p-değeri ve t-testleri | `10_hafta/` |
| 9 | 17 Aralık | Hipotez testi II: ki-kare ve ANOVA | `10_hafta/` |
| 10 | 24 Aralık | Korelasyon, basit ve çoklu regresyon | `11_hafta/`, `12_hafta/` |
| 11 | 31 Aralık | Lojistik regresyon ve genel tekrar | `13_hafta/` |
| — | 4–17 Ocak 2027 | **FİNAL SINAVI** | — |

Ayrıntı ve okuma atamaları için izlenceye bakınız.

---

## Değerlendirme

| | |
|---|---|
| Ara Sınav (Vize) | **%40** |
| Yarıyıl Sonu Sınavı (Final) | **%60** |

Proje, ödev, kısa sınav ve katılım notu **yoktur.** Her oturumun ardından
yayımlanan alıştırmalar ve cevap anahtarları **notlandırılmaz**; kendinizi
sınamanız içindir. Sınav soruları bu alıştırmalarla aynı biçimde kurgulanır.

---

## Depo yapısı

```
IST2083/
├── izlence/         Ders izlencesi
├── 01_hafta/ ...     Haftalık ders notları, sunumlar, alıştırmalar
├── data/            Tüm veri setleri (tek merkez)
├── images/          Görseller
├── IST2083.Rproj    RStudio proje dosyası — çalışmaya bunu açarak başlayın
└── README.md
```

**Klasör numaraları ile oturum numaraları aynı değildir.** Klasör adları
dersin ilk yılından gelen sıralamayı korur; hangi oturumda hangi klasörün
işleneceğini yukarıdaki tablodan görebilirsiniz.

### Veri dosyalarını okuma

Tüm veri setleri `data/` klasöründedir ve `here` paketiyle çağrılır:

```r
library(here)
veri <- read.csv(here("data", "example_data.csv"))
```

`here()`, proje kökünü `IST2083.Rproj` dosyasından bulur. Bu sayede kod
hem sizde hem bizde, hem Windows'ta hem macOS'ta aynı şekilde çalışır.
**Kendi bilgisayarınıza özel mutlak yol yazmayın** (`C:/Users/...` veya
`~/Desktop/...` gibi).

---

## Ders ortamı

İki seçenekten birini kullanabilirsiniz:

- **RStudio (yerel)** — dersin ana anlatım ortamı. Kurulum rehberine bakınız.
- **GitHub Codespaces (bulut)** — tarayıcıda çalışır, kurulum gerektirmez.
  Kılavuzda anlatılmıştır.

---

## Soru ve sorun bildirme

- **Ders içeriğiyle ilgili sorular:** hakan.mehmetcik@marmara.edu.tr
- **Teknik sorunlar** (kurulum, paket hatası, çalışmayan kod): bu deponun
  **Issues** sekmesini kullanın. Böylece aynı sorunu yaşayan arkadaşlarınız
  da cevabı görür.

Issue açarken hatayı üreten **en kısa kod parçasını** ve **hata mesajının
tamamını** yapıştırın; ekran görüntüsü yerine metin tercih edilir.
