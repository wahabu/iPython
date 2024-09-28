# Write a Python program to sovle (x + y) * (x + y).
# Test Data: x = 4, y = 3
# Expected Output: (4 + 3) ^ 2) = 49

# Define variables 'x' and 'y' and assign values to them.
x, y = 4, 3
# Calculate the result by squaring the sum of 'x' and 'y'.
result = x * x + 2 * x * y + y * y
# Print the result with a formatted message.
print("({} + {}) ^ 2 = {}".format(x, y, result))