# - Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.

# Define a function 'test_number5' that takes two integer inputs: x and y.
def test_number5(x, y):
  # Check if any of the following conditions are met:
  # 1. x is equal to y.
  # 2. The absolute difference between x and y is equal to 5.
  # 3. The sum of x and y is equal to 5.
  if x == y or abs(x - y) == 5 or (x + y) == 5:
    # If any of the conditions are met, return True.
    return True
  else:
    # If none of the conditions are met, return False.
    return False
  
# Test the 'test_number5' functions with different sets of input values and print the results.
print(test_number5(int(input("Enter first number: ")), int(input("Enter second number: "))))
print(test_number5(int(input("Enter first number: ")), int(input("Enter second number: "))))
print(test_number5(int(input("Enter first number: ")), int(input("Enter second number: "))))
print(test_number5(int(input("Enter first number: ")), int(input("Enter second number: "))))
print(test_number5(int(input("Enter first number: ")), int(input("Enter second number: "))))
