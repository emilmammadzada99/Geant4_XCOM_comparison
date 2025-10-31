import pandas as pd
import re 
import matplotlib.pyplot as plt

file_xcom = "build/al.txt"

energies_xcom = []
total_with_coh_xcom = []

with open(file_xcom, "r") as f:
    for line in f:
        if re.match(r'\s*\d\.\d+E[+-]\d{2}', line):
            parts = line.split()
            if len(parts) >= 8:
                energy = float(parts[0])
                total_with = float(parts[-2])  # "WITH COHERENT SCATT."
                energies_xcom.append(energy)
                total_with_coh_xcom.append(total_with)


df_xcom = pd.DataFrame({
    "Photon Energy (MeV)": energies_xcom,
    "Total Attenuation With Coherent (cm2/g)": total_with_coh_xcom
})


print(df_xcom.head(10))


file_geant = "build/g4_cm2_g.txt"

energies_geant = []
cross_sections_geant = []


with open(file_geant, "r") as f:
    for line in f:
        match = re.search(r'Energy:\s*([\d\.Ee+-]+)\s*MeV.*?Total cross section per mass:\s*([\d\.Ee+-]+)', line)
        if match:
            energy = float(match.group(1))
            sigma = float(match.group(2))
            energies_geant.append(energy)
            cross_sections_geant.append(sigma)

df_geant = pd.DataFrame({
    "Photon Energy (MeV)": energies_geant,
    "Total Cross Section per Mass (cm²/g)": cross_sections_geant
})


print(df_geant.head(10))

plt.figure(figsize=(8, 5))
plt.loglog(energies_xcom, total_with_coh_xcom, marker='x', linestyle='-', linewidth=1.5, markersize=4,label="XCOM",color='red')
plt.loglog(energies_geant, cross_sections_geant, marker='o', linestyle='none', linewidth=1.5, markersize=4,label="Geant4",color='blue')
plt.xlabel("Photon Energy (MeV)", fontsize=12)
plt.ylabel("(cm²/g)", fontsize=12)
plt.title("XCOM-Geant4 Total Mass Attenuation Coefficient Aluminium", fontsize=13)
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("xcom_geant4_plot.png", dpi=300, bbox_inches="tight")
plt.show()
