# ---------------------------------------------------------------------------------
# - Write a Python program to convert height (in feet and inches) to centimeters.
# ---------------------------------------------------------------------------------

# Prompt the user to input their height.
print("Input your height: ")

# Reat the feet part of the height and convert it to an integer.
h_ft = int(input("Feet: "))

# Read the inches part of the height and convert it to an integer.
h_inch = int(input("Inches: "))

# Convert the height from feet and inches to inches.
h_inch += h_ft * 12

# Calculate the height in centimeters by multiplying by the conversion factor (2.54).
h_cm = round(h_inch * 2.54, 1)

# Print the calculated height in centimeters.
print("Your height is: %d cm." % h_cm)