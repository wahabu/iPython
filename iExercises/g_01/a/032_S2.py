# --------------------------------------------------------------------------------------------
# - Write a Python program to find the least common multiple (LCM) of two positive integers.
# --------------------------------------------------------------------------------------------


# define a function 'lcm' that calculates the least common multiple (LCM) of two numbers, 'x' and 'y'.
def lcm(x, y):
    # Compare 'x' and 'y' to determine the larger number and store it in 'z'.
    if x > y:
        z = x
    else:
        z = y  
    # Use a 'while' loop to find the LCM.
    while True:
        # Check if 'z' is divisible by both 'x' and 'y' with no remainder.
        if (z % x == 0) and (z % y == 0):
            # If both conditions are met, 'z' is the LCM, so store it in 'lcm' and break the loop.
            lcm = z
            break
        # If the conditions are not met, increment 'z' and continue checking.
        z += 1
        
    # Return the calculated LCM
    return lcm

# Calculate and print the LCM of 4 and 6.
print(lcm(4, 6))
# Calculate and print the LCM of 15 and 17.
print(lcm(15, 17))