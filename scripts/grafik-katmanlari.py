# -*- coding: utf-8 -*-
"""
IST2083 — Modül 03 görseli: grafiklerin dilbilgisi katmanları.
Özgün üretim (matplotlib). Çıktı: 03_modul/images/grafik-katmanlari.png
Yeniden üretmek için (proje kökünden):  python3 scripts/grafik-katmanlari.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams["font.family"] = "DejaVu Sans"

MOR   = "#4C3A80"
MAVI  = "#2E6E8E"
GRI   = "#5A5A5A"
KOYU  = "#20202A"
ACIK  = "#F2F0F7"
ACIK2 = "#EAF1F5"
ACIK3 = "#F4F4F4"

# (katman adı, ggplot2 karşılığı, sorduğu soru, zorunlu mu)
KATMANLAR = [
    ("Veri",       "ggplot(data = ...)",            "Hangi tablo? Her satır neyi temsil ediyor?", True),
    ("Eşleme",     "aes(x = , y = , color = ...)",  "Hangi sütun hangi görsel özelliğe gidecek?", True),
    ("Geom",       "geom_point(), geom_col() ...",  "Veri hangi şekille çizilecek?",             True),
    ("Stat",       "stat = \"count\", \"identity\"", "Çizmeden önce veri özetlenecek mi?",        False),
    ("Konum",      "position = \"stack\" / \"dodge\" / \"fill\"", "Üst üste binen şekiller nasıl yerleşecek?", False),
    ("Ölçek",      "scale_x_log10(), scale_fill_*()", "Veri değeri görsel değere nasıl çevrilecek?", False),
    ("Koordinat",  "coord_cartesian(), coord_polar()", "Çizim hangi düzlemde yapılacak?",          False),
    ("Faset",      "facet_wrap(~ degisken)",        "Grafik alt gruplara bölünecek mi?",          False),
    ("Tema",       "theme_minimal(), labs(title = ...)", "Başlık, etiket ve veriyle ilgisi olmayan görünüm", False),
]

fig, ax = plt.subplots(figsize=(10.4, 7.6))
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")

ax.text(50, 97, "Bir ggplot2 Grafiğinin Katmanları", ha="center", va="center",
        fontsize=17, fontweight="bold", color=KOYU)
ax.text(50, 92.3, "İlk üç katman zorunludur; geri kalanların her birinin makul bir varsayılanı vardır",
        ha="center", va="center", fontsize=10.5, color=GRI, style="italic")

ust = 86
yuk = 8.2
aralik = 1.1
for i, (ad, kod, soru, zorunlu) in enumerate(KATMANLAR):
    y = ust - (i + 1) * yuk - i * aralik + yuk
    y0 = y - yuk
    renk = MOR if zorunlu else MAVI
    dolgu = ACIK if zorunlu else ACIK2
    ax.add_patch(FancyBboxPatch((3, y0), 94, yuk - 0.6,
                                boxstyle="round,pad=0.35,rounding_size=1.2",
                                linewidth=1.6, edgecolor=renk, facecolor=dolgu))
    ax.text(6, y0 + (yuk - 0.6) / 2, f"{i + 1}", ha="center", va="center",
            fontsize=12, fontweight="bold", color=renk)
    ax.text(9.5, y0 + (yuk - 0.6) / 2, ad, ha="left", va="center",
            fontsize=12.5, fontweight="bold", color=renk)
    ax.text(26, y0 + (yuk - 0.6) / 2 + 1.5, soru, ha="left", va="center",
            fontsize=10.2, color=KOYU)
    ax.text(94, y0 + (yuk - 0.6) / 2, "zorunlu" if zorunlu else "isteğe bağlı",
            ha="right", va="center", fontsize=9.5, fontweight="bold" if zorunlu else "normal",
            color=renk, style="normal" if zorunlu else "italic")
    ax.text(26, y0 + (yuk - 0.6) / 2 - 1.7, kod, ha="left", va="center",
            fontsize=9.2, color=GRI, family="DejaVu Sans Mono")

ax.text(50, -1.5, "ggplot(veri, aes(...))  +  geom_*()  +  scale_*()  +  facet_*()  +  theme_*()",
        ha="center", va="center", fontsize=10, color=GRI, family="DejaVu Sans Mono")

fig.savefig("03_modul/images/grafik-katmanlari.png", dpi=200, bbox_inches="tight",
            facecolor="white")
print("03_modul/images/grafik-katmanlari.png üretildi")
