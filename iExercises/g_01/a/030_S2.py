# --------------------------------------------------------------------------------------------------
# - Write a Python program that will accept the base and height of a triangle and compute its area.
# --------------------------------------------------------------------------------------------------

# Prompt the user to input the base and height of a triangle as integers.
b = int(input("Input the base: "))
h = int(input("Input the height: "))

# Calculate the area of the triangle using the formula: (base * height) /2.
area = b * h / 2

# Print the calculated area of the triangle.
print("area = ", area)