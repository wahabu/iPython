# - Write a Python program to calculate the hypotenuse of a right angled triangle.

import math
a = int(input("Enter the side right size: "))
b = int(input("Enter the side right size: "))

c = math.sqrt(a ** 2 + b ** 2)

print(int(c))
