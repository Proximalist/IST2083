# -*- coding: utf-8 -*-
"""
IST2083 — Modül 08 görseli: Standart normal dağılımın yoğunluk
fonksiyonu (mean=0, sd=1). Özgün üretim (matplotlib + scipy).
Çıktı: 08_modul/images/normal.png
Yeniden üretmek için (proje kökünden):  python3 scripts/normal-dagilimi.py

Not: Bu görsel önceden İngilizce etiketlerle üretilmişti; 08. modül
denetiminde fark edilip Türkçe olarak yeniden üretildi
(bkz. docs/belge-standardi.md §5 ve §8).
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

plt.rcParams["font.family"] = "DejaVu Sans"

MAVI = "#2E4E8E"
KOYU = "#20202A"
GRI = "#5A5A5A"

x = np.linspace(-4, 4, 600)
yogunluk = stats.norm.pdf(x, 0, 1)

fig, ax = plt.subplots(figsize=(7.2, 4.4))
ax.plot(x, yogunluk, color=MAVI, lw=2.4, label="Normal Dağılım (μ=0, σ=1)")

ax.set_title("Standart Normal Dağılım", fontsize=13, fontweight="bold",
             color=KOYU, pad=10)
ax.set_xlabel("Değer", fontsize=10.5, color=KOYU)
ax.set_ylabel("Yoğunluk", fontsize=10.5, color=KOYU)
ax.legend(loc="upper right", fontsize=9, frameon=False)
for s in ["top", "right"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(GRI)
ax.spines["left"].set_color(GRI)
ax.tick_params(colors=GRI)

fig.tight_layout()
fig.savefig("08_modul/images/normal.png", dpi=200, bbox_inches="tight", facecolor="white")
print("kaydedildi: 08_modul/images/normal.png")
