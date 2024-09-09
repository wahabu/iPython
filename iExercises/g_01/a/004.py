# -----------------------------------------------------------------------------
# -- Calculates the area of a circle based on the radius entered by the user --
# -- Sample Output: -----------------------------------------------------------
# -- r = 1.1 ------------------------------------------------------------------
# -- Area = 3.8013271108436504 ------------------------------------------------

# Import the 'pi' constant from the 'math' module to calculate the area of a circle
from math import pi

# Prompt the user to input the radius of the circle
radius = float(input("Enter the Radius of your circle: "))

# Calculate the area of the circle using the formula: area = π * r^2
area = pi * radius ** 2

# Display the result, including the radius and calculated area
print(f"Area = {area}")