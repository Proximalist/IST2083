# -*- coding: utf-8 -*-
"""
IST2083 — Modül 08 görseli: standart normal dağılımda %95 yüzdelik
değeri (x ≈ 1.645) ve altında kalan kümülatif olasılık alanı.
Özgün üretim (matplotlib + scipy).
Çıktı: 08_modul/images/kumulatif2.png
Yeniden üretmek için (proje kökünden):  python3 scripts/kumulatif2.py

Not: Bu görsel dosya adıyla üretilmişti ama kaynak betiği depoda
yoktu; 08. modül denetiminde fark edilip geriye dönük eklendi
(bkz. docs/belge-standardi.md §5).
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

plt.rcParams["font.family"] = "DejaVu Sans"

MAVI = "#1F4EBF"
ACIK = "#B9D6EA"
KIRMIZI = "#C0392B"
KOYU = "#20202A"
GRI = "#5A5A5A"

esik = stats.norm.ppf(0.95)  # ~1.645

x = np.linspace(-4, 4, 600)
yogunluk = stats.norm.pdf(x)
sol = x <= esik

fig, ax = plt.subplots(figsize=(7.4, 4.4))
ax.plot(x, yogunluk, color=MAVI, lw=2.2, label="Normal Dağılım (μ=0, σ=1)")
ax.fill_between(x[sol], yogunluk[sol], color=ACIK, alpha=0.8,
                 label=r"Kümülatif Olasılık: $P(X \leq x)$")
ax.axvline(esik, color=KIRMIZI, ls="--", lw=1.3,
           label=f"95. Yüzdelik Değer: x = {esik:.2f}")

ax.set_title("Standart Normal Dağılım: %95 Yüzdelik Değer",
              fontsize=12.5, fontweight="bold", color=KOYU, pad=10)
ax.set_xlabel("X Değerleri", fontsize=10.5, color=KOYU)
ax.set_ylabel("Yoğunluk", fontsize=10.5, color=KOYU)
ax.legend(loc="upper left", fontsize=8.3, frameon=True)
for s in ["top", "right"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(GRI)
ax.spines["left"].set_color(GRI)
ax.tick_params(colors=GRI)

fig.tight_layout()
fig.savefig("08_modul/images/kumulatif2.png", dpi=200, bbox_inches="tight", facecolor="white")
print("kaydedildi: 08_modul/images/kumulatif2.png")
