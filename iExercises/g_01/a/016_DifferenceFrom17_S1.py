# ---------------------------------------------------------------------------------------
# -- Write a Python program to calculate the difference between a given number and 17. 
# -- If the number is greater than 17, return twice the absolute difference. 
# ---------------------------------------------------------------------------------------

# Prompt the user to input the number
num = int(input("Input any number: "))


# Define a function named "difference" that takes an integer parameter 'n'
def difference(n):
  # Check if n is n is less than or equal to 17
  if n <= 17:
    # If n is less than or equal to 17, return the absolute difference between 17 and n
    return 17 - n
  else:
    # If n is greater than 17, return the absolute difference between n and 17 multiplied by 2
    return (n - 17) * 2
  
# Call the "difference" function with the argument num and print the result
print(difference(num))