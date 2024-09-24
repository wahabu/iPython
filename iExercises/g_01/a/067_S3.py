# - Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.
# ------------------------------------------------------------------

# Prompt the user to iput the pressure in kilopascals and store it as a floating-point number.
kpa = float(input("Input the pressure in kilopascals > "))

# Calculate the pressure in pounds per square inch (psi) and round it to 3 decimal places.
pressure_in_psi = round(kpa * 0.145038, 3)

# Calculate the pressure in millimeters of mercury (mmHg) and round it to 3 decimal places.
pressure_in_mmHg = round(kpa * 7.50062, 3)

# Calculate the pressure in standard atmospheres (atmp) and round it to 3 decimal places.
pressure_in_atmp = round(kpa * 0.0098692382432766, 3)

# Display the calculated pressure values in psi, mmHg, and atmp using an f-string.
print(f"Pressure = {pressure_in_psi} psi \nor {pressure_in_mmHg} mmHg \nor {pressure_in_atmp} atmp")