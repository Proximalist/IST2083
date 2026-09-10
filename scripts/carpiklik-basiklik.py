# -*- coding: utf-8 -*-
"""
IST2083 — Modül 04 görseli: çarpıklık (sağa/sola/simetrik) ve
basıklık (leptokurtik/mezokurtik/platikurtik) tipolojisi.
Özgün üretim (matplotlib + scipy). Çıktı: 04_modul/images/carpiklik-basiklik.png
Yeniden üretmek için (proje kökünden):  python3 scripts/carpiklik-basiklik.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

plt.rcParams["font.family"] = "DejaVu Sans"

MOR   = "#4C3A80"
MAVI  = "#2E6E8E"
GRI   = "#5A5A5A"
KOYU  = "#20202A"
ACIK  = "#F2F0F7"
ACIK2 = "#EAF1F5"

fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.6))

# --- Sol panel: çarpıklık ---
ax = axes[0]
x = np.linspace(-4, 8, 800)

sola = stats.skewnorm.pdf(x, -8, loc=2.6, scale=2.4)      # sola çarpık (negatif)
simetrik = stats.norm.pdf(x, loc=1, scale=1.15)            # simetrik
saga = stats.skewnorm.pdf(x, 8, loc=-1.4, scale=2.4)        # sağa çarpık (pozitif)

ax.plot(x, simetrik, color=KOYU, lw=2.2, label="Simetrik (çarpıklık ≈ 0)")
ax.plot(x, saga, color=MOR, lw=2.2, label="Sağa çarpık (pozitif, > 0)")
ax.plot(x, sola, color=MAVI, lw=2.2, label="Sola çarpık (negatif, < 0)")

ax.fill_between(x, simetrik, color=KOYU, alpha=0.06)
ax.fill_between(x, saga, color=MOR, alpha=0.10)
ax.fill_between(x, sola, color=MAVI, alpha=0.10)

ax.set_title("Çarpıklık (Skewness)", fontsize=13, fontweight="bold", color=KOYU, pad=10)
ax.set_ylim(0, max(sola.max(), simetrik.max(), saga.max()) * 1.42)
ax.set_yticks([])
ax.set_xticks([])
ax.legend(loc="upper left", fontsize=8.3, frameon=False)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(GRI)
ax.annotate("uzun kuyruk sağda\n→ ortalama > medyan", xy=(5.2, 0.03), fontsize=7.6,
            color=MOR, ha="center")
ax.annotate("uzun kuyruk solda\n→ ortalama < medyan", xy=(-0.3, 0.03), fontsize=7.6,
            color=MAVI, ha="center")

# --- Sağ panel: basıklık ---
ax2 = axes[1]
xx = np.linspace(-5, 5, 800)

lepto = stats.laplace.pdf(xx, scale=0.85)       # leptokurtik: sivri, kalın kuyruk
mezo  = stats.norm.pdf(xx, scale=1.0)           # mezokurtik: normal (referans)
plati = stats.uniform.pdf(xx, loc=-2.6, scale=5.2) * 1.05  # platikurtik: yayvan

ax2.plot(xx, mezo, color=KOYU, lw=2.2, label="Mezokurtik (basıklık ≈ 3, normal)")
ax2.plot(xx, lepto, color=MOR, lw=2.2, label="Leptokurtik (sivri, kalın kuyruklu)")
ax2.plot(xx, plati, color=MAVI, lw=2.2, label="Platikurtik (yayvan, ince kuyruklu)")

ax2.fill_between(xx, mezo, color=KOYU, alpha=0.06)

ax2.set_title("Basıklık (Kurtosis)", fontsize=13, fontweight="bold", color=KOYU, pad=10)
ax2.set_ylim(0, max(lepto.max(), mezo.max(), plati.max()) * 1.35)
ax2.set_yticks([])
ax2.set_xticks([])
ax2.legend(loc="upper right", fontsize=8.3, frameon=False)
for s in ["top", "right", "left"]:
    ax2.spines[s].set_visible(False)
ax2.spines["bottom"].set_color(GRI)

fig.suptitle("Dağılımın Şekli: Çarpıklık ve Basıklık", fontsize=15, fontweight="bold",
             color=KOYU, y=1.03)
fig.tight_layout()
fig.savefig("04_modul/images/carpiklik-basiklik.png", dpi=200, bbox_inches="tight",
            facecolor="white")
print("kaydedildi: 04_modul/images/carpiklik-basiklik.png")
