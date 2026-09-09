# -*- coding: utf-8 -*-
"""
IST2083 — 2. hafta görseli: R'ın dört temel veri yapısının tipolojisi.
Özgün üretim (matplotlib). Çıktı: 02_modul/images/veri-yapilari-tipolojisi.png
Yeniden üretmek için:  python3 scripts/veri-yapilari-tipolojisi.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch

plt.rcParams["font.family"] = "DejaVu Sans"

MOR   = "#4C3A80"
MAVI  = "#2E6E8E"
GRI   = "#5A5A5A"
ACIK  = "#F2F0F7"
ACIK2 = "#EAF1F5"

fig, ax = plt.subplots(figsize=(10.2, 6.8))
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")

ax.text(56, 97, "R'ın Dört Temel Veri Yapısı", ha="center", va="center",
        fontsize=17, fontweight="bold", color="#20202A")
ax.text(56, 92, "İki soru sorarak hangisine ihtiyacınız olduğunu bulursunuz",
        ha="center", va="center", fontsize=10.5, color=GRI, style="italic")

# --- Eksen soruları ---------------------------------------------------
ax.text(56, 85.5, "SORU 1:  Veri kaç boyutlu?", ha="center", va="center",
        fontsize=10.5, fontweight="bold", color=GRI)
ax.text(2.5, 55, "SORU 2:  Elemanların türü aynı olmak zorunda mı?",
        ha="center", va="center", fontsize=10.5, fontweight="bold",
        color=GRI, rotation=90)

ax.text(42, 79.5, "1 boyutlu  (tek sıra)", ha="center", va="center",
        fontsize=11, fontweight="bold", color="#20202A")
ax.text(83, 79.5, "2 boyutlu  (satır × sütun)", ha="center", va="center",
        fontsize=11, fontweight="bold", color="#20202A")
ax.text(14, 62, "EVET\nhepsi aynı tür\n(homojen)", ha="center", va="center",
        fontsize=10, fontweight="bold", color="#20202A", linespacing=1.5)
ax.text(14, 33, "HAYIR\ntürler karışık\n(heterojen)", ha="center", va="center",
        fontsize=10, fontweight="bold", color="#20202A", linespacing=1.5)

# --- Dört kutu --------------------------------------------------------
def kutu(x, y, w, h, baslik, kod, ornek, renk, dolgu):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.6,rounding_size=1.6",
                                linewidth=1.8, edgecolor=renk, facecolor=dolgu))
    ax.text(x + w/2, y + h - 5.5, baslik, ha="center", va="center",
            fontsize=12.5, fontweight="bold", color=renk)
    ax.text(x + w/2, y + h - 11.5, kod, ha="center", va="center",
            fontsize=10.5, family="monospace", color="#20202A")
    ax.text(x + w/2, y + 6.5, ornek, ha="center", va="center",
            fontsize=9.2, family="monospace", color=GRI, linespacing=1.5)

kutu(26, 49, 32, 26, "Vektör",     "c()",          'c(4, 7, 2, 9)',                 MAVI, ACIK2)
kutu(67, 49, 32, 26, "Matris",     "matrix()",     'matrix(1:6,\n       nrow = 2)',  MAVI, ACIK2)
kutu(26, 20, 32, 26, "Liste",      "list()",       'list(ad = "Ali",\n     yas = 25)', MOR, ACIK)
kutu(67, 20, 32, 26, "Data Frame", "data.frame()", 'data.frame(\n  ad = ..., yas = ...)',   MOR, ACIK)

# --- Kutuların dışına taşan iki not -----------------------------------
ax.add_patch(FancyArrowPatch((30, 21.5), (24, 13.5), arrowstyle="-|>", mutation_scale=13,
                             linewidth=1.4, color=MOR, linestyle=(0, (4, 2))))
ax.text(23, 11.5,
        "Liste bu tablodan taşar: bir listenin içinde\nbaşka bir liste (hatta bir data frame) olabilir.",
        ha="center", va="top", fontsize=8.8, color=MOR, linespacing=1.6)

ax.add_patch(FancyArrowPatch((86, 21.5), (86, 13.5), arrowstyle="-|>", mutation_scale=13,
                             linewidth=1.4, color=MOR, linestyle=(0, (4, 2))))
ax.text(86, 11.5,
        "Data frame aslında özel bir listedir:\nher sütun ayrı bir vektördür.",
        ha="center", va="top", fontsize=8.8, color=MOR, linespacing=1.6)

ax.text(56, 2, "IST2083 — Temel İstatistik ve R ile Veri Analizi",
        ha="center", va="center", fontsize=8, color="#9A9AA5")

fig.savefig("02_modul/images/veri-yapilari-tipolojisi.png",
            dpi=200, bbox_inches="tight", facecolor="white")
print("üretildi")
