# - Write a Python program to sum three given integers.
# - However, if two values are equal, the sum will be zero.
# -----------------------------------------------------------

x = int(input("Input First number: "))
y = int(input("Input Second number: "))
z = int(input("Input Third number: "))

if x == y and x != z:
    sum = 0
    print(f"{x} + {y} + {z} = {sum}")
elif x != y and x == z:
    sum = 0
    print(f"{x} + {y} + {z} = {sum}")
elif x != y and y == z:
    sum = 0
    print(f"{x} + {y} + {z} = {sum}")
else:
    sum = x + y + z
    print(f"{x} + {y} + {z} = {sum}")

