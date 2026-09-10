# Codespaces / devcontainer

Bu klasör, dersin **kurulum gerektirmeyen** çalışma ortamını tanımlar.
Öğrenci GitHub'da depoyu açıp *Code → Codespaces → Create codespace*
dediğinde, aşağıdaki ortam tarayıcıda hazır gelir:

- **R 4.4** ve tidyverse (rocker imajından)
- **Quarto 1.6.40** ve TinyTeX (PDF üretimi için)
- `scripts/paketler.R` ile kurulan ders paketleri

## Neden sürümler sabitlendi

Bu depoda, sürüm farklarından kaynaklanan üç ayrı hata yaşandı:
macOS'ta çalışıp Linux'ta kırılan Unicode dosya adları, yalnızca bir
klasörde bulunan görseller ve TeX Live 2024 ile 2026 arasındaki paket
uyuşmazlığı. Sürümleri sabitlemenin amacı, öğrencinin makinesi,
Codespaces ve CI'ın **aynı** sonucu üretmesidir.

R paketlerinin sürümleri henüz kilitli değil. `renv` kurulumu için
depo kökünde şunu çalıştırın:

```r
install.packages("renv")
renv::init()
```

Bu, `renv.lock` üretir. Dosya depoya eklendikten sonra
`postCreateCommand` satırını `Rscript -e 'renv::restore()'` olarak
değiştirmek gerekir.
