# IST2083 — Belge Standardı

Bu belge, depodaki tüm ders belgelerinin **dosya adlandırması** ve **YAML
başlığı** için tek geçerli kuralı tanımlar. Yeni bir belge üretirken bu
sayfaya bakılır; istisna yapılmaz.

## 1. Klasör adları

```
NN_hafta/          NN = 01 … 14, daima iki haneli
```

İki hane zorunludur: aksi hâlde hem `ls` hem GitHub dosya listesi
`10, 11, 12, 13, 14, 1, 2, 3 …` sırasıyla dizer ve klasörler karışır.

> **Not:** Klasör numarası, izlencedeki **oturum** numarasıyla aynı
> değildir. İzlence 3. oturum `05_hafta/` ve `06_hafta/` klasörlerini
> kullanır. Klasör numarası bir *modül* numarasıdır; hangi oturumda hangi
> modülün işlendiği yalnızca izlence tablosunda tanımlıdır.

## 2. Dosya adları

```
NN_hafta_<tur>[_<ek>].qmd
```

`<tur>` sabit bir sözlükten seçilir:

| `<tur>` | Belge |
|---|---|
| `ders` | Haftanın ders notu (ana içerik) |
| `sunum` | Derste yansıtılan revealjs sunumu |
| `lab` | Derste birlikte yapılan rehberli uygulama |
| `alistirmalar` | Çoktan seçmeli alıştırma seti |
| `cevap_anahtari` | Alıştırmaların gerekçeli cevapları |

`<ek>` yalnızca **aynı türden birden fazla belge** varsa kullanılır:
`06_hafta_ders_olasilik.qmd`, `14_hafta_alistirmalar_1.qmd`.

Kurallar:

- Dosya adı klasör adını tekrar eder (`02_hafta/02_hafta_ders.qmd`).
  Gereksiz görünür ama gereklidir: RStudio sekme çubuğu yalnızca dosya
  adını gösterir; üç haftanın `ders.qmd` dosyası açıkken hangisinin
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
title: "N. Hafta: Konu Başlığı"
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
title: "N. Hafta: Konu Başlığı"
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

`.pdf` ve `.html` çıktıları ile `*_files/` klasörleri **depoda
tutulmaz** (bkz. `.gitignore`). Kaynak `.qmd` değiştiğinde çıktı
bayatlar ve depoda içerikle uyuşmayan bir belge kalır. Öğrenciye
sunulacak nihai PDF üretimi CI'a bırakılmıştır.

Tek istisna: `14_hafta/SIMD 2020 INDICATOR DESCRIPTIONS.pdf` — bu bir
render çıktısı değil, veri setinin kaynak dokümantasyonudur.

## 5. Görsel yolları

Görseller belgenin **kendi klasöründeki** `images/` altında tutulur
(`02_hafta/images/...`) ve belgede `images/dosya.png` biçiminde,
göreli olarak çağrılır. RStudio belgeleri kendi klasörlerine göre
render eder; proje köküne göre yazılan yollar (`../images/...`)
çalışmaz.

Görsel dosya adlarında Türkçe karakter kullanılmaz (bkz. §2).
