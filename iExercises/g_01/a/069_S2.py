# Write a Python program to sort three integers without using conditional statements and loops.

# Prompt the user to input three integers and convert them to variables x, y, and z.
x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))

# Find the minium value among x, y, and z and store it in variable a1.
a1 = min(x, y, z)

# Find the maximum value among x, y, and z and store it in variable a3.
a3 = max(x, y, z)

# Calculate the middle value (not the minimum or maximum) by subtracting a1 and a3 from the sum of x, y, and z.
a2 = (x + y + z) - a1 - a3

# Print the numbers in sorted order (a1, a2, a3).
print("Numbers in sorted order: ", a1, a2, a3)