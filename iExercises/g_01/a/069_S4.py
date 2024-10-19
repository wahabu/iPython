# Write a Python program to sort three integers without using loops.

def sort_numbers(x, y, z):
    if x >= y:
        max_xy = x
    else:
        max_xy = y
    
    if max_xy >= z:
        max_xyz = max_xy
    else:
        max_xyz = z
    
    if x <= y:
        min_xy = x
    else:
        min_xy = y
        
    if min_xy <= z:
        min_xyz = min_xy
    else:
        min_xyz = z
    
    middle = (x + y + z) - max_xyz - min_xyz
    
    return min_xyz, middle, max_xyz

print(sort_numbers(8, 1, 3))
print(sort_numbers(8, 3, 1))
print(sort_numbers(3, 8, 1))
print(sort_numbers(1, 8, 3))
print(sort_numbers(3, 1, 8))
print(sort_numbers(1, 3, 8))
print(sort_numbers(3, 3, 2))