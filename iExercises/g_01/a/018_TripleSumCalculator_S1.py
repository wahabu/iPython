# -----------------------------------------------------------------------------
# -- Write a Python program to calculate the sum of three given numbers.
# -- If the values are equal, return three times their sum.
# -----------------------------------------------------------------------------


# Define a function named "sum_thrice" that takes three integer parameters: x, y, and z
def sum_thrice(x, y, z):
  # Calculate the sum of x, y, and z
  sum = x + y + z
  
  # Check if x, y, and z are all equal (all three numbers are the same)
  if x == y == z:
    # If they are equal, triple the sum
    sum = sum * 3
    
  # Return the final sum
  return sum

# Prompt the user to input numbers
x = int(input("Input the first number: "))
y = int(input("Input the second number: "))
z = int(input("Input the third number: "))

# Call the "sum_thrice" function with the arguments (x, y, z) and print the result
print(sum_thrice(x, y, z))
