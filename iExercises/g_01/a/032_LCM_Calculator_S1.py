# ------------------------------------------------------------------------------------------
# - Write a Python program to find the least common multiple (LCM) of two positive integers.
# ------------------------------------------------------------------------------------------

# Define a function to calculate the greatest common divisor (GCD) of two numbers.
def gcd(x, y):
    # Initialize gcd to 1.
    gcd = 1

    # Check if y is a divisor of x (x is divisible by y).
    if x % y == 0:
        return y

    # Iterate from half of y down to 1.
    for k in range(int(y / 2), 0, -1):
    # Check if both x and y are divisible by k.
        if x % k == 0 and y % k == 0:
        # Update the GCD to the current value of k and exit the loop.
            gcd = k
            break

    # Return the calculated GCD.
    return gcd

# Define a function to calculate the least common multiple (LCM) of two positive integers.
def lcm(x, y):
    return y * (int(x/gcd(x, y)))

# Print the LCM of specific pairs of numbers.
print("GCD of your first & second numbers is: ", lcm(int(input("Input first number: ")), int(input("Input second number: "))))            