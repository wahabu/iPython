# Write a Python program to sort three integers without using conditinal statements and loops.

def sort_numbers(x, y, z):
    max_xy = (x >= y) * x + (x < y) * y
    
    max_xyz = (max_xy >= z) * max_xy + (max_xy < z) * z
    
    min_xy = (x <= y) * x + (x > y) * y
    min_xyz = (min_xy <= z) * min_xy + (min_xy > z) * z
    
    middle = (x + y + z) - max_xyz - min_xyz
    
    return min_xyz, middle, max_xyz

print(sort_numbers(8, 1, 3))
print(sort_numbers(8, 3, 1))
print(sort_numbers(3, 8, 1))
print(sort_numbers(1, 8, 3))
print(sort_numbers(3, 1, 8))
print(sort_numbers(1, 3, 8))
print(sort_numbers(3, 3, 2))