# Geant4_XCOM_comparison
Geant4 vs XCOM photon cross section comparison and plotting
## Installation and Running XCOM

To download, compile, and run the XCOM program, follow these steps:

```bash
# Download XCOM from NIST
wget https://physics.nist.gov/PhysRefData/Xcom/XCOM.tar.gz

# Extract the archive
tar -xvzf XCOM.tar.gz
cd XCOM

# Update system packages and install gfortran
sudo apt update
sudo apt install gfortran

# Compile the Fortran source
gfortran -std=legacy -o XCOM XCOM.f

# Run the program
./XCOM
#
Program XCOM, Version 3.1
M.J.Berger and J.H.Hubbell, 23 June 1999

Enter name of substance:
al

Options for characterization of substance:
   1. Elemental substance, specified by atomic number
   2. Elemental substance, specified by chemical symbol
   3. Compound, specified by chemical formula
   4. Mixture of elements and/or compounds
Enter choice: 1

Enter atomic number of element:
13

Options for output quantities:
   1. Cross sections in barns/atom
   2. Cross sections in barns/atom, and
      attenuation coefficients in cm2/g
   3. Partial interaction coefficients and
      attenuation coefficients in cm2/g
Enter choice: 2

Options for energy list for output data:
   1. Standard energy grid only
   2. Standard grid plus additional energies
   3. Additional energies only
Enter choice: 1

Specify file on which output (cross section table) is to be stored:
al.txt

Calculation is finished.
```
