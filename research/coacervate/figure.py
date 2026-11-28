import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from model import simulate

PAPER, INK, MUTED, GREEN, RUST, LINE = "#eeeade", "#202a29", "#69716a", "#648477", "#ad654a", "#c9c4b5"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "axes.edgecolor": MUTED,
                     "axes.labelcolor": INK, "xtick.color": MUTED, "ytick.color": MUTED,
                     "text.color": INK, "figure.facecolor": PAPER, "axes.facecolor": PAPER})

fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.6), dpi=200)
cols = {1: MUTED, 10: GREEN, 50: RUST}
for K in (1, 10, 50):
    t, ci, co, r = simulate(P=0.5, K=K, T=400)
    a.plot(t, r, color=cols[K], lw=2.2, label=f"K = {K}")
    a.axhline(K, color=cols[K], ls=":", lw=1)
a.set_xlabel("время (условные единицы)")
a.set_ylabel("c внутри / c снаружи")
a.set_title("A. Селективность: капля копит вещество до K", loc="left", fontsize=11)
a.legend(frameon=False, loc="upper left")
a.set_ylim(0, 55)

for P in (0.05, 0.5, 5.0):
    t, ci, co, r = simulate(P=P, K=10, T=150)
    b.plot(t, r, lw=2.2, label=f"P = {P}")
b.axhline(10, color=INK, ls=":", lw=1)
b.set_xlabel("время (условные единицы)")
b.set_ylabel("c внутри / c снаружи")
b.set_title("B. Проницаемость задаёт скорость, но не предел (K = 10)", loc="left", fontsize=11)
b.legend(frameon=False, loc="upper left")
b.set_xscale("log")
b.set_ylim(0, 12)

for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.text(0.01, 0.01, "Иллюстративная модель: параметры условные, не откалиброваны по опытам Опарина.",
         fontsize=8.5, color=MUTED)
fig.tight_layout(rect=(0, 0.04, 1, 1))
fig.savefig("coacervate_uptake.svg")
fig.savefig("coacervate_uptake.png")
print("ok")
