# Modül 05 (Veri İşleme: dplyr/tidyr) için türetilmiş öğretim verisi
#
# Bu betik iki küçük veri seti üretir:
#   1. data/orgutler.csv ve data/orgut_uyelikleri.csv — join (birleştirme)
#      örnekleri için, gapminder ülkeleriyle eşleşen bölgesel örgüt
#      üyelik verisi (AB, NATO, ASEAN, MERCOSUR).
#   2. data/gapminder_genis_yasam_beklentisi.csv — pivot_longer örneği
#      için, Gapminder Vakfı'nın site üzerinden dağıttığı ham biçime
#      (yıllar sütunlarda) benzer GENİŞ formatlı bir dosya.
#
# Ülke adları gapminder paketindeki `country` faktör düzeyleriyle
# BİREBİR eşleşecek şekilde yazılmıştır (ör. "Slovak Republic", "Turkey").
# Üyelik listeleri, ilgili örgütün gerçek üye listesinden yalnızca
# gapminder'ın 142 ülkelik panelinde YER ALAN ülkelere indirgenmiştir;
# bu kasıtlıdır ve ders notunda "veri kapsamı her zaman tam değildir"
# noktasını göstermek için kullanılır (bkz. anti_join örneği).
#
# Çalıştırma: Rscript scripts/veri-uretimi-05-modul.R

library(dplyr)
library(tidyr)
library(gapminder)
library(readr)

# --- 1. Örgüt bilgi tablosu ------------------------------------------------
orgutler <- tibble::tribble(
  ~orgut_kodu, ~orgut_adi,                              ~kurulus_yili,
  "AB",        "Avrupa Birliği",                        1993L,
  "NATO",      "Kuzey Atlantik Antlaşması Örgütü",       1949L,
  "ASEAN",     "Güneydoğu Asya Uluslar Birliği",         1967L,
  "MERCOSUR",  "Güney Ortak Pazarı",                     1991L
)

# --- 2. Üyelik tablosu (uzun format: ülke-örgüt başına bir satır) ---------
ab_uyeleri <- c(
  "Austria", "Belgium", "Bulgaria", "Croatia", "Czech Republic", "Denmark",
  "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy",
  "Netherlands", "Poland", "Portugal", "Romania", "Slovak Republic",
  "Slovenia", "Spain", "Sweden"
)

nato_uyeleri <- c(
  "Albania", "Belgium", "Bulgaria", "Canada", "Croatia", "Czech Republic",
  "Denmark", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland",
  "Italy", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal",
  "Romania", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Turkey",
  "United Kingdom", "United States"
)

asean_uyeleri <- c(
  "Cambodia", "Indonesia", "Malaysia", "Myanmar", "Philippines",
  "Singapore", "Thailand", "Vietnam"
)

mercosur_uyeleri <- c("Argentina", "Brazil", "Paraguay", "Uruguay")

orgut_uyelikleri <- bind_rows(
  tibble::tibble(ulke = ab_uyeleri, orgut_kodu = "AB"),
  tibble::tibble(ulke = nato_uyeleri, orgut_kodu = "NATO"),
  tibble::tibble(ulke = asean_uyeleri, orgut_kodu = "ASEAN"),
  tibble::tibble(ulke = mercosur_uyeleri, orgut_kodu = "MERCOSUR")
) |>
  arrange(orgut_kodu, ulke)

# Doğrulama: tüm ülke adları gapminder'da var mı?
gapminder_ulkeleri <- unique(as.character(gapminder::gapminder$country))
eslesmeyen <- setdiff(orgut_uyelikleri$ulke, gapminder_ulkeleri)
if (length(eslesmeyen) > 0) {
  stop("gapminder ile eşleşmeyen ülke adı: ", paste(eslesmeyen, collapse = ", "))
}

write_csv(orgutler, "data/orgutler.csv")
write_csv(orgut_uyelikleri, "data/orgut_uyelikleri.csv")

message("orgutler.csv: ", nrow(orgutler), " satır")
message("orgut_uyelikleri.csv: ", nrow(orgut_uyelikleri), " satır")

# --- 3. Geniş formatlı gapminder (pivot_longer örneği için) ---------------
# Gapminder Vakfı'nın kendi sitesinden indirilen gösterge dosyaları
# gerçekte bu biçimde gelir: her ülke bir satır, her yıl bir sütun.
gapminder_genis <- gapminder::gapminder |>
  select(country, continent, year, lifeExp) |>
  pivot_wider(names_from = year, values_from = lifeExp) |>
  arrange(continent, country)

write_csv(gapminder_genis, "data/gapminder_genis_yasam_beklentisi.csv")
message("gapminder_genis_yasam_beklentisi.csv: ", nrow(gapminder_genis), " satır x ",
        ncol(gapminder_genis), " sütun")
