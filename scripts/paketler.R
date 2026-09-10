# IST2083 — ders belgelerinin ihtiyaç duyduğu R paketleri
#
# İki işi vardır:
#   1. Yeni bir ortamda (yerel makine, Codespaces, CI) paketleri kurar.
#   2. renv.lock üretilirken hangi paketlerin kilitleneceğini belirler.
#
# Kullanım:  Rscript scripts/paketler.R

# --- Denetimden geçmiş modüllerin (01, 02) ve izlencenin ihtiyaçları ---
temel <- c(
  "knitr", "rmarkdown",   # render altyapısı
  "here",                 # proje köküne göre dosya yolu
  "ggplot2", "dplyr",     # görselleştirme ve veri işleme
  "gapminder",            # 01. modülde kullanılan örnek veri seti
  "readxl", "writexl"     # Excel okuma/yazma
)

# --- Henüz denetlenmemiş modüllerin (03-14) ek ihtiyaçları -------------
# Bu modüller _quarto.yml render listesinde kapalı; paketleri de
# şimdilik isteğe bağlı. Modül denetimden geçtikçe ilgili satırlar
# yukarıdaki "temel" vektörüne taşınır.
ek <- c(
  "tidyverse", "tidyr", "lubridate", "scales", "patchwork",
  "kableExtra", "janitor", "haven", "fst",
  "nycflights13", "mosaicData", "NHANES", "mdsr", "macleish", "fec16",
  "ggmosaic", "wesanderson",
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
