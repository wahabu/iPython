# Write a Python program to calculate the hypotenuse of a right angled triangle.

# Import the sqrt function from the math module to calculate the square root.
from math import sqrt

# Prompt the user to input the lengths of the shorter triangle sides.
print("Input lengths of shorter triangle sides: ")

# Read and convert the input for side 'a' to a floating-point number.
a = float(input("a: "))

# Read and convert the input for side 'b' to a floating-point number.
b = float(input("b: "))

# Calculate the length of the hypotenuse using the Pythagorean theorem.
c = sqrt(a**2 + b**2)

# Print the calculated length of the hypotenuse.
print("The length of the hypotenuse is: ", c)