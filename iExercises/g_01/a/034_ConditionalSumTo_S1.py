# - Write a Python program to sum two given integers.
# - However, if the sum is between 15 and 20 it will return 20.

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

def special_number(x, y):
    sum = x + y
    if sum >= 15 and sum <= 20:
        sum = 20
        return sum
      
    else:
        return sum
      
print(special_number(x, y))