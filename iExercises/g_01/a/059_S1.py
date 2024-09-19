# ---------------------------------------------------------------------------------
# - Write a Python program to convert height (in feet and inches) to centimeters.
# ---------------------------------------------------------------------------------

height_feet = int(input("Input the feet value: ")) # 5
height_inches = int(input("Input the inch value: ")) # 9+11/16
centimeters_ft = 30.48 * height_feet
centimeters_in = 2.54 * height_inches
total = centimeters_in + centimeters_ft
height_cm = int(centimeters_in + centimeters_ft)
if total - height_cm >= 0.5:
  height_cm += 1
else:
  height_cm
print(height_cm)