# --------------------------------------------------------------------------------------------------
# - Write a Python program that will accept the base and height of a triangle and compute its area.
# --------------------------------------------------------------------------------------------------

def triangle_area(b, h):
  return (1/2) * b * h 

b = int(input("Input base of triangle: "))
h = int(input("Input height of triangle: "))

print(triangle_area(b, h))