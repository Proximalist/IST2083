# -*- coding: utf-8 -*-
"""
IST2083 — Modül 08 görseli: Poisson dağılımının olasılık kütle fonksiyonu
(mu=3). Özgün üretim (matplotlib + scipy).
Çıktı: 08_modul/images/poison.png
Yeniden üretmek için (proje kökünden):  python3 scripts/poisson-dagilimi.py

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

YESIL = "#2E8B6E"
KOYU = "#20202A"
GRI = "#5A5A5A"

mu = 3
k = np.arange(0, 15)
olasilik = stats.poisson.pmf(k, mu)

fig, ax = plt.subplots(figsize=(7.2, 4.4))
ax.bar(k, olasilik, color=YESIL, edgecolor="white", width=0.72, label="Poisson OKF")

ax.set_title(f"Poisson Dağılımı (μ={mu})", fontsize=13, fontweight="bold",
             color=KOYU, pad=10)
ax.set_xlabel("Olay Sayısı (k)", fontsize=10.5, color=KOYU)
ax.set_ylabel("Olasılık  " + r"$P(X=k)$", fontsize=10.5, color=KOYU)
ax.set_xticks(k)
ax.legend(loc="upper right", fontsize=9, frameon=False)
for s in ["top", "right"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(GRI)
ax.spines["left"].set_color(GRI)
ax.tick_params(colors=GRI)

fig.tight_layout()
fig.savefig("08_modul/images/poison.png", dpi=200, bbox_inches="tight", facecolor="white")
print("kaydedildi: 08_modul/images/poison.png")
