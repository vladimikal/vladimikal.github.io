"""Minimal coacervate uptake model (illustrative, not calibrated).

A droplet of volume VD sits in a bath of volume VB that initially holds
solute at concentration C0. The droplet takes up solute through a boundary
with permeability P and partitions it with coefficient K (inside/outside
equilibrium ratio, the 'selectivity').

    dN/dt = P * (c_out - N / (VD * K))
    c_out = (N_total - N) / VB,   N_total = C0 * VB

N is the amount inside the droplet. Equilibrium: c_in = K * c_out.
Euler integration with a small step; all units arbitrary.
"""
import numpy as np

def simulate(P=0.5, K=10.0, VD=1.0, VB=1000.0, C0=1.0, T=40.0, dt=1e-3):
    n = int(T / dt) + 1
    t = np.linspace(0, T, n)
    N = 0.0
    Ntot = C0 * VB
    c_in = np.zeros(n)
    c_out = np.zeros(n)
    c_out[0] = C0
    for i in range(1, n):
        co = (Ntot - N) / VB
        dN = P * (co - N / (VD * K)) * dt
        N += dN
        c_in[i] = N / VD
        c_out[i] = (Ntot - N) / VB
    ratio = c_in / c_out
    return t, c_in, c_out, ratio

if __name__ == "__main__":
    for K in (1, 10, 50):
        t, ci, co, r = simulate(P=0.5, K=K)
        print(f"K={K:>3}: ratio at t=5 {r[int(5/0.001)]:.2f}, t=40 {r[-1]:.2f}, c_in end {ci[-1]:.2f}")
    for P in (0.05, 0.5, 5.0):
        t, ci, co, r = simulate(P=P, K=10)
        half = np.argmax(r >= 0.5 * r[-1])
        print(f"P={P:>4}: time to half of final ratio {t[half]:.2f}, final ratio {r[-1]:.2f}")
