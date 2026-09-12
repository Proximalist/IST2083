# IST2083 — ders belgelerinin ihtiyaç duyduğu R paketleri
#
# İki işi vardır:
#   1. Yeni bir ortamda (yerel makine, Codespaces, CI) paketleri kurar.
#   2. renv.lock üretilirken hangi paketlerin kilitleneceğini belirler.
#
# Kullanım:  Rscript scripts/paketler.R

# --- Denetimden geçmiş modüllerin (bkz. _quarto.yml render listesi) ve izlencenin ihtiyaçları ---
temel <- c(
  "knitr", "rmarkdown",   # render altyapısı
  "here",                 # proje köküne göre dosya yolu
  "ggplot2", "dplyr",     # görselleştirme ve veri işleme
  "tidyr",                # 05. modülde pivot_longer()/pivot_wider()
  "readr",                # 05. modülde read_csv() ile veri okuma
  "scales",               # 03. modülde eksen biçimlendirme (label_dollar)
  "gapminder",            # 01., 03., 05., 10. ve 11. modülde kullanılan sürekli veri seti
  "mosaicData",           # 03. modülde Simpson paradoksu örneği (SAT verisi)
  "ggrepel",              # 03. modülde Gamson grafiğinde parti etiketleme
  "patchwork",            # 03. modülde Minard grafiğinde iki paneli birleştirme
  "readxl", "writexl",    # Excel okuma/yazma
  "gtsummary",            # 04. modülde yayına hazır "Tablo 1" özeti
  "mdsr"                  # 11. modülde SAT_2010 veri seti (öğretmen maaşı - SAT puanı örneği)
)

# --- Henüz denetlenmemiş modüllerin (12-14) ek ihtiyaçları -------------
# Bu modüller _quarto.yml render listesinde kapalı; paketleri de
# şimdilik isteğe bağlı. Modül denetimden geçtikçe ilgili satırlar
# yukarıdaki "temel" vektörüne taşınır.
ek <- c(
  "tidyverse", "lubridate",
  "kableExtra", "janitor", "haven", "fst",
  "nycflights13", "NHANES", "macleish", "fec16",
  "ggmosaic", "ggthemes", "wesanderson",
  "AER", "coefplot", "pscl", "nnet", "mlogit"
)

kur <- function(paketler) {
  eksik <- paketler[!paketler %in% rownames(installed.packages())]
  if (length(eksik) == 0) {
    message("Tüm paketler zaten kurulu.")
  } else {
    message("Kurulacak: ", paste(eksik, collapse = ", "))
    install.packages(eksik)
  }
}

args <- commandArgs(trailingOnly = TRUE)
if (length(args) > 0 && args[1] == "hepsi") kur(c(temel, ek)) else kur(temel)
