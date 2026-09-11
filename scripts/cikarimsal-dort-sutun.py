# -*- coding: utf-8 -*-
"""
IST2083 — Modül 06 görseli: çıkarımsal istatistiğin dört sütunu
(örnekleme, tahmin, hipotez testi, regresyon/modelleme) → çıkarımsal istatistik.
Özgün üretim (matplotlib). Çıktı: 06_modul/images/cikarimsal-dort-sutun.png

Not: Bu görsel, eski images/yorumlayici.png dosyasının yerini alır.
Eski dosya, kutunun içinde standart olmayan "Yorumlayıcı İstatistik"
terimini kullanıyordu; doğru terim "Çıkarımsal İstatistik"tir.
Yeniden üretmek için (proje kökünden):  python3 scripts/cikarimsal-dort-sutun.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams["font.family"] = "DejaVu Sans"

MOR   = "#4C3A80"
MAVI  = "#2E6E8E"
GRI   = "#5A5A5A"
KOYU  = "#20202A"
ACIK  = "#F2F0F7"
ACIK2 = "#EAF1F5"

renkler = ["#2E6E8E", "#3E8E6E", "#8E8E2E", "#8E5A2E"]
etiketler = ["Örnekleme", "Tahmin", "Hipotez Testi", "Regresyon/Modelleme"]

fig, ax = plt.subplots(figsize=(10, 5.4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")

sol_x, sag_x = 1.3, 7.4
ys = [8.1, 6.0, 3.9, 1.8]

for y, etiket, renk in zip(ys, etiketler, renkler):
    box = FancyBboxPatch((sol_x - 1.1, y - 0.5), 2.2, 1.0,
                          boxstyle="round,pad=0.08,rounding_size=0.15",
                          linewidth=1.6, edgecolor=renk, facecolor=ACIK)
    ax.add_patch(box)
    ax.text(sol_x, y, etiket, ha="center", va="center", fontsize=10.5,
             fontweight="bold", color=KOYU)
    arrow = FancyArrowPatch((sol_x + 1.1, y), (sag_x - 0.9, 5.0),
                             arrowstyle="-|>", mutation_scale=14,
                             linewidth=1.4, color=renk, alpha=0.85,
                             connectionstyle="arc3,rad=0.0")
    ax.add_patch(arrow)

sonuc = FancyBboxPatch((sag_x - 0.9, 4.2), 2.6, 1.6,
                        boxstyle="round,pad=0.1,rounding_size=0.18",
                        linewidth=2.0, edgecolor=KOYU, facecolor=ACIK2)
ax.add_patch(sonuc)
ax.text(sag_x + 0.4, 5.0, "Çıkarımsal\nİstatistik", ha="center", va="center",
         fontsize=12.5, fontweight="bold", color=KOYU)

ax.set_title("Çıkarımsal İstatistiğin Dört Sütunu", fontsize=15,
             fontweight="bold", color=KOYU, pad=16)

fig.tight_layout()
fig.savefig("06_modul/images/cikarimsal-dort-sutun.png", dpi=200,
            bbox_inches="tight", facecolor="white")
print("kaydedildi: 06_modul/images/cikarimsal-dort-sutun.png")
