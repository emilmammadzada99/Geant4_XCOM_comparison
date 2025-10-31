# xcom energy_modifier.py
energies = [
    1.00E-03, 1.50E-03, 1.56E-03, 1.56E-03, 2.00E-03, 3.00E-03, 4.00E-03, 5.00E-03, 6.00E-03,
    8.00E-03, 1.00E-02, 1.50E-02, 2.00E-02, 3.00E-02, 4.00E-02, 5.00E-02, 6.00E-02, 8.00E-02,
    1.00E-01, 1.50E-01, 2.00E-01, 3.00E-01, 4.00E-01, 5.00E-01, 6.00E-01, 8.00E-01, 1.00E+00,
    1.02E+00, 1.25E+00, 1.50E+00, 2.00E+00, 2.04E+00, 3.00E+00, 4.00E+00, 5.00E+00, 6.00E+00,
    7.00E+00, 8.00E+00, 9.00E+00, 1.00E+01, 1.10E+01, 1.20E+01, 1.30E+01, 1.40E+01, 1.50E+01,
    1.60E+01, 1.80E+01, 2.00E+01, 2.20E+01, 2.40E+01, 2.60E+01, 2.80E+01, 3.00E+01, 4.00E+01,
    5.00E+01, 6.00E+01, 8.00E+01, 1.00E+02, 1.50E+02, 2.00E+02, 3.00E+02, 4.00E+02, 5.00E+02,
    6.00E+02, 8.00E+02, 1.00E+03, 1.50E+03, 2.00E+03, 3.00E+03, 4.00E+03, 5.00E+03, 6.00E+03,
    8.00E+03, 1.00E+04, 1.50E+04, 2.00E+04, 3.00E+04, 4.00E+04, 5.00E+04, 6.00E+04, 8.00E+04,
    1.00E+05
]

template = """\
#
/testem/det/setMat G4_Al
/gun/particle gamma 
/gun/energy {energy} MeV
/run/setCut 10 mm
/run/beamOn
#
"""

with open("al.mac", "w") as file:
    
    file.write("""\
# Macro file for "TestEm0.cc"
#
/control/verbose 0
/run/verbose 1
#
#/testem/phys/addPhysics local
/testem/phys/addPhysics emstandard_opt3
#
#/process/eLoss/verbose 0
/process/em/printParameters 
#
/run/initialize
#
# Disable energy loss fluctuations
#/process/eLoss/fluctuation off

# Limit max step length (example 25 um, adjust if needed)
#/step/max 25 um
#
#
""")
    
    for energy in energies:
        file.write(template.format(energy=energy))
        file.write("\n") 
