# - Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.
# ----------------------------------------------------------------

# Prompt the user to input pressure in kilopascals and convert it to a floating-point number.
kpa = float(input("Input pressure in kilopascals: "))

# Convert kilopascals to pounds per square inch (psi) using the conversion factor.
psi = kpa / 6.89475729

# Convert kilopascals to millimeters of mercury (mmHg) using the conversion factor.
mmhg = kpa * 760 / 101.325

# Convert kilopascals to atmospheres (atm) using the conversion factor.
atm = kpa / 101.325

# Print the pressure in pounds per square inch (psi) with 2 decimal places.
print("The pressure in pounds per square inch: %.2f psi" % (psi))

# Print the pressure in millimeters of mercury (mmHg) with 2 decimal places.
print("The pressure in millimeters of mercury: %.2f mmHg" % (mmhg))

# Print the atmosphere pressure (atm) with decimal places.
print("Atmosphere pressure: %.2f atm." % (atm))