# Write a Python program to swap two variables.

# Swap two variables in Python

a, b = 30, 20
print(f"Before swap: a = {a}, b = {b}")

# Pythonic swap using tuple unpacking
a, b = b, a

print(f"After swap:  a = {a}, b = {b}")