# -*- coding: utf-8 -*-
"""
IST2083 — Modül 08 görseli: Binom dağılımının olasılık kütle fonksiyonu
(n=10, p=0.5). Özgün üretim (matplotlib + scipy).
Çıktı: 08_modul/images/binom.png
Yeniden üretmek için (proje kökünden):  python3 scripts/binom-dagilimi.py

Not: Bu görsel önceden İngilizce etiketlerle (Matplotlib varsayılan
stiliyle) üretilmişti; 08. modül denetiminde fark edilip Türkçe olarak
yeniden üretildi (bkz. docs/belge-standardi.md §5 ve §8).
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

plt.rcParams["font.family"] = "DejaVu Sans"

MAVI = "#2E6E8E"
KOYU = "#20202A"
GRI = "#5A5A5A"

n, p = 10, 0.5
k = np.arange(0, n + 1)
olasilik = stats.binom.pmf(k, n, p)

fig, ax = plt.subplots(figsize=(7.2, 4.4))
ax.bar(k, olasilik, color=MAVI, edgecolor="white", width=0.72, label="Binom OKF")

ax.set_title(f"Binom Dağılımı (n={n}, p={p})", fontsize=13, fontweight="bold",
             color=KOYU, pad=10)
ax.set_xlabel("Başarı Sayısı (k)", fontsize=10.5, color=KOYU)
ax.set_ylabel("Olasılık  " + r"$P(X=k)$", fontsize=10.5, color=KOYU)
ax.set_xticks(k)
ax.legend(loc="upper right", fontsize=9, frameon=False)
for s in ["top", "right"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(GRI)
ax.spines["left"].set_color(GRI)
ax.tick_params(colors=GRI)

fig.tight_layout()
fig.savefig("08_modul/images/binom.png", dpi=200, bbox_inches="tight", facecolor="white")
print("kaydedildi: 08_modul/images/binom.png")
