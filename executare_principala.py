from functii_utilitare import *
from algoritmi_sat import *
import time

fisier_intrare = "clauze1.txt"
clauze = incarca_clauze_din_fisier(fisier_intrare)

print("\n------- Rezolvare prin Rezoluție -------")
start = time.perf_counter()
rezolutie(clauze, afiseaza=True)
end = time.perf_counter()
print(f"Rezoluția a durat {end - start:.6f} secunde.")

print("\n------- Algoritm DP -------")
clauze = incarca_clauze_din_fisier(fisier_intrare)
start = time.perf_counter()
algoritm_dp(clauze, afiseaza=True)
end = time.perf_counter()
print(f"Algoritmul DP a durat {end - start:.6f} secunde.")

print("\n------- Algoritm DPLL -------")
clauze = incarca_clauze_din_fisier(fisier_intrare)
start = time.perf_counter()
dpll_cu_afisare(clauze, afiseaza=True)
end = time.perf_counter()
print(f"Algoritmul DPLL a durat {end - start:.6f} secunde.")
