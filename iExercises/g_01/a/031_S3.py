# ----------------------------------------------------------------------------------------------------
# - Write a Python program that computes the greatest common divisor (GCD) of three positive integers.
# ----------------------------------------------------------------------------------------------------

# Define a function to calculate the greatest common divisor (GCD) of three numbers.
def gcd(x, y, z):
    # Initialize gcd to 1.
    gcd = 1

    # Check if z is a divisor of x and z is a divisor of y(x is divisible by z and y is divisible by z).
    if x % z == 0 and y % z == 0:
        return z

    # Iterate from half of y down to 1.
    for k in range(int(z / 2), 0, -1):
    # Check if both x and y are divisible by k.
        if x % k == 0 and y % k == 0 and z % k == 0:
        # Update the GCD to the current value of k and exit the loop.
            gcd = k
            break

    # Return the calculated GCD.
    return gcd

# Print the GCD of specific pairs of numbers.
print("GCD of your first & second & third numbers is: ", gcd(int(input("Input first number: ")), int(input("Input second number: ")), int(input("Input third number: "))))