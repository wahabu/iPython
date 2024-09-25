# - Write a Python program to sum two given integers.
# - However, if the sum is between 15 and 20 it will return 20.
# ---------------------------------------------------------------


# Define a function 'sum' that takes two integer inputs: x and y.
def sum(x, y):
    # Calculate the sum of x and y and store it in the 'sum' variable.
    sum = x + y
    # Check if the calculated sum is within the range [15, 20) (inclusive on 15, exclusive on 20).
    if sum in range(15, 20):
        # If the sum is within the range, return 20.
        return 20
    else:
        # If the sum is outside the range, return the calculated sum.
        return sum
      
print(sum(int(input()), int(input())))