# -----------------------------------------------------------------------------
# -- Calculates the area of a circle based on the radius entered by the user --
# -- Sample Output: -----------------------------------------------------------
# -- r = 1.1 ------------------------------------------------------------------
# -- Area = 3.8013271108436504 ------------------------------------------------
import math

python_pi = math.pi
radius = float(input("What\'s Radius of your circle?"))
area = python_pi * (radius * radius)
print(f"Area = {area}")