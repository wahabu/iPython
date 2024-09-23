# - Write a Python program to convert pressure in kilopascals to pounds per square inch,
# - a millimeter of mercury (mmHg) and atmosphere pressure.
# ----------------------------------------------------------------------------------------

kPa = int(input("Enter your pressure in kilopascals: "))

# pressure in psi = pressure in kPa × 0.1450377.
psi = kPa * 0.1450377

# Atmospheric pressure = PSI ÷ 14.6959.
atmosphere = psi / 14.6959

# mmHg value = kPa value x 7.50062
mmHg = kPa * 7.50062

print(f"PSI = {psi},pmmHg = {mmHg}, and atmosphere = {atmosphere}")