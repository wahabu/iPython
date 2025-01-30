# - Write a Python program to convert the distance (in feet) to inches, yards, and miles.
# -----------------------------------------------------------------------------------------

# Prompt the user to input a distance in feet and store it in the variable 'd_ft'.
d_ft = int(input("Input distance in feet: "))

# Convert the distance in feet to inches and store it in the variable d_in'.
d_in = d_ft * 12

# Convert the distance in feet to yards and store it in the variable 'd_yd'.
d_yd = d_ft / 3.0

# Convert the distance in feet to miles and store it in the variable 'd_mi'.
d_mi = d_ft / 5280.0

# Print the calculated distances in inches, yards, and miles.
print("The distance in inches is %i inches." % d_in)
print("The distance in yards is %.2f yards." % d_yd)
print("The distance in miles is %.3f miles." % d_mi)
