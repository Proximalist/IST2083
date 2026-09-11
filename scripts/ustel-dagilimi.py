# -*- coding: utf-8 -*-
"""
IST2083 — Modül 08 görseli: Üstel dağılımın yoğunluk fonksiyonu
(ölçek parametresi 1/λ = 1). Özgün üretim (matplotlib + scipy).
Çıktı: 08_modul/images/ustsel.png
Yeniden üretmek için (proje kökünden):  python3 scripts/ustel-dagilimi.py

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

TURUNCU = "#C97A2B"
KOYU = "#20202A"
GRI = "#5A5A5A"

olcek = 1  # 1/lambda
x = np.linspace(0, 4, 600)
yogunluk = stats.expon.pdf(x, scale=olcek)

fig, ax = plt.subplots(figsize=(7.2, 4.4))
ax.plot(x, yogunluk, color=TURUNCU, lw=2.4, label="Üstel Dağılım (1/λ=1)")

ax.set_title("Üstel Dağılım", fontsize=13, fontweight="bold", color=KOYU, pad=10)
ax.set_xlabel("Süre", fontsize=10.5, color=KOYU)
ax.set_ylabel("Yoğunluk", fontsize=10.5, color=KOYU)
ax.legend(loc="upper right", fontsize=9, frameon=False)
for s in ["top", "right"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(GRI)
ax.spines["left"].set_color(GRI)
ax.tick_params(colors=GRI)

fig.tight_layout()
fig.savefig("08_modul/images/ustsel.png", dpi=200, bbox_inches="tight", facecolor="white")
print("kaydedildi: 08_modul/images/ustsel.png")
