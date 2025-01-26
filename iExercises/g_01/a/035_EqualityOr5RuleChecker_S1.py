# - Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.

# Prompt the user for input the first integer number
x = int(input("Input first number: "))

# prompt the user for input the second integer number
y = int(input("Input second number: "))

# Define a function 'check_values' that takes two integer inputs: x and y
def check_values(x, y):
  if x == y or abs(x+y) == 5 or abs(x-y) == 5:
    return True
  else:
    print(abs(x + y))
    return False

# Check the values five function with different sets of input values and print the results.
print(check_values(x, y))