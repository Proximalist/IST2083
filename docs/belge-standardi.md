# IST2083 — Belge Standardı

Bu belge, depodaki tüm ders belgelerinin **dosya adlandırması** ve **YAML
başlığı** için tek geçerli kuralı tanımlar. Yeni bir belge üretirken bu
sayfaya bakılır; istisna yapılmaz.

## 0. Oturum mu, modül mü?

Depo iki farklı numaralandırma kullanır ve bunlar **kasten** birbirinden
ayrıdır:

- **Oturum**, takvimdeki bir ders günüdür (1. oturum = 1 Ekim). Yalnızca
  izlencede geçer. Dönem içinde tatil, telafi veya iptal olduğunda
  değişebilir.
- **Modül**, bir konu paketidir (`05_modul/` = veri işleme). Depodaki
  klasör ve dosya adları modül numarasını taşır ve bu numara dönem
  boyunca **değişmez**.

İkisi bire bir eşleşmez: 3. oturum iki modülü birden işler
(`05_modul/` + `06_modul/`), 10. modül ise iki oturuma yayılır (8. ve
9. oturum). Hangi oturumda hangi modülün işleneceği **yalnızca
izlencedeki tabloda** tanımlıdır; başka hiçbir yerde tekrarlanmaz ki
çelişme ihtimali olmasın.

Bu yüzden belge başlıkları "5. Hafta" demez, **"Modül 05"** der.
Ders notlarının **metni içinde** ise oturum numarası kullanılır
("3. oturumda `dplyr` göreceğiz"), çünkü öğrenci için anlamlı olan
takvimdir.

## 1. Klasör adları

```
NN_modul/          NN = 01 … 14, daima iki haneli
```

İki hane zorunludur: aksi hâlde hem `ls` hem GitHub dosya listesi
`10, 11, 12, 13, 14, 1, 2, 3 …` sırasıyla dizer ve klasörler karışır.

## 2. Dosya adları

```
NN_modul_<tur>[_<ek>].qmd
```

`<tur>` sabit bir sözlükten seçilir:

| `<tur>` | Belge |
|---|---|
| `ders` | Modülün ders notu (ana içerik) |
| `sunum` | Derste yansıtılan revealjs sunumu |
| `lab` | Derste birlikte yapılan rehberli uygulama |
| `alistirmalar` | Çoktan seçmeli alıştırma seti |
| `cevap_anahtari` | Alıştırmaların gerekçeli cevapları |

`<ek>` yalnızca **aynı türden birden fazla belge** varsa kullanılır:
`06_modul_ders_olasilik.qmd`, `14_modul_alistirmalar_1.qmd`.

Kurallar:

- Dosya adı klasör adını tekrar eder (`02_modul/02_modul_ders.qmd`).
  Gereksiz görünür ama gereklidir: RStudio sekme çubuğu yalnızca dosya
  adını gösterir; üç modülün `ders.qmd` dosyası açıkken hangisinin
  hangisi olduğu ayırt edilemez.
- Türkçe karakter, boşluk ve büyük harf **kullanılmaz**. Dosya adları
  yalnızca `a-z`, `0-9` ve `_` içerir. Gerekçe: macOS'un dosya
  adlarını Unicode olarak normalize etme biçimi Linux'unkinden farklıdır;
  `ı`, `ğ`, `ü` içeren yollar Codespaces ve CI'da sessizce kırılabilir.
- Uzantı daima `.qmd`'dir. `.Rmd` kullanılmaz.

## 3. YAML başlığı

Tüm belgeler `lang`'e kadar **birebir aynıdır**; yalnızca `title`,
isteğe bağlı `subtitle` ve `format` bloğu değişir.

### Ders notu, lab, alıştırma, cevap anahtarı (PDF)

```yaml
---
title: "Modül NN: Konu Başlığı"
subtitle: "yalnızca lab/alıştırma/cevap anahtarı için"
author: "Prof. Dr. Hakan Mehmetcik"
date: "`r Sys.Date()`"
lang: tr
format: pdf
editor: visual
execute:
  echo: true
  warning: true
  message: false
  cache: false
df-print: kable
---
```

### Sunum (revealjs)

```yaml
---
title: "Modül NN: Konu Başlığı"
author: "Prof. Dr. Hakan Mehmetcik"
date: "`r Sys.Date()`"
lang: tr
format:
  revealjs:
    theme: simple
    slide-number: true
    toc: true
    toc-depth: 2
    incremental: true
    code-overflow: scroll
    code-line-numbers: false
    transition: fade
    math: mathjax
editor: visual
execute:
  echo: true
  warning: false
  message: false
  cache: false
df-print: kable
---
```

### Alanların gerekçesi

- **`date`** — daima `Sys.Date()` çağrısıyla verilir; sabit tarih yazılmaz. Sabit tarihler bir
  önceki dönemden kalır ve belgenin bayat olduğunu gizler.
- `lang: tr` — Quarto'nun otomatik ürettiği etiketleri Türkçeleştirir
  ("Figure" → "Şekil", "Contents" → "İçindekiler") ve LaTeX'in Türkçe
  heceleme kurallarını devreye sokar.
- `warning: true` (ders notunda) — R'ın uyarıları öğretici olduğu için
  öğrenciye gösterilir. Sunumda `false`, çünkü slayt düzenini bozar.
- `message: false` — `library()` çağrılarının paket yükleme mesajları
  gösterilmez.
- `cache: false` — önbellek, veri değiştiğinde sessizce eski sonuç
  gösterebilir; ders belgelerinde bu risk alınmaz.
- **`output: asis` kullanılmaz.** Bu bir öbek seçeneğidir; `execute:`
  altında genel olarak verildiğinde `df-print: kable` çıktısını ham
  LaTeX/HTML olarak basar.

## 4. Render çıktıları

Render edilmiş `.pdf` / `.html` belgeler ve revealjs sunumlarının
`*_files/` klasörleri **depoda tutulur.** Gerekçe: öğrenci kaynak
dosyayı kendi bilgisayarında render edemediğinde (paket eksik, LaTeX
kurulu değil, Codespaces kotası dolmuş) hazır belgeye erişebilmelidir.

Bunun bir bedeli vardır ve kural budur:

> **Bir `.qmd` dosyasını düzenlediyseniz, aynı commit'te onu yeniden
> render edip çıktısını da ekleyin.** Unutulursa depoda içerikle
> uyuşmayan bir belge kalır ve öğrenci yanlış sürümü okur.

Bu kural, CI kurulana kadar elle uygulanır. CI kurulduğunda render
otomatikleşir ve bu madde yeniden değerlendirilir.

İstisnalar: `figure-pdf/` ve `figure-latex/` ara figür klasörleri
izlenmez (nihai PDF'e zaten gömülürler). `_calisma/`, `sinav/` ve
`notlar/` klasörleri hiçbir koşulda izlenmez.

## 5. Görsel yolları

Görseller belgenin **kendi klasöründeki** `images/` altında tutulur
(`02_modul/images/...`) ve belgede `images/dosya.png` biçiminde,
göreli olarak çağrılır. RStudio belgeleri kendi klasörlerine göre
render eder; proje köküne göre yazılan yollar (`../images/...`)
çalışmaz.

Görsel dosya adlarında Türkçe karakter kullanılmaz (bkz. §2).

Kod ile üretilen görsellerin kaynak betiği `scripts/` altında,
görselle aynı adı taşıyacak biçimde tutulur ve proje kökünden
çalıştırılır:

```
python3 scripts/veri-yapilari-tipolojisi.py
```

Böylece görsel yeniden üretilebilir kalır; PNG'yi elden düzeltmek
yerine betik düzenlenir.

## 6. Yeni bir modül denetimden geçtiğinde

Modül elden geçirildikten sonra iki dosyada birer satır güncellenir:

1. **`_quarto.yml`** — o modülün satırındaki `#` kaldırılır, böylece
   `quarto render` ve CI onu da render etmeye başlar.
2. **`scripts/paketler.R`** — modülün kullandığı paketler `ek`
   vektöründen `temel` vektörüne taşınır; CI iş akışındaki paket
   listesine de eklenir.

Bu iki adım atlanırsa modül CI tarafından hiç sınanmaz ve Linux'ta
kırık olduğu fark edilmez.
