# Write a Python program to calculate the midpoints of a line.

x1 = float(input("Input x of first point: "))
y1 = float(input("Input y of first point: "))
x2 = float(input("Input x of second point: "))
y2 = float(input("Input y of second point: "))

point_1 = (x1 + x2) / 2.0
point_2 = (y1 + y2) / 2.0

print("The midpoints = (", point_1, ", ", point_2, ")")
