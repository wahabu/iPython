# - Write a Python program to solve (x + y) * (x + y).
# - Test Data: x = 4, y = 3
# - Expected Output: (4 + 3) ^ 2 = 49

# Prompt the user for input the first integer number
x = int(input("Input first number: "))
# Prompt the user for input the second integer number
y = int(input("Input second number: "))

solve = x**2 + 2 * x * y + y**2

print("Test Data: x = %d, y = %d" % (x, y))

print("Expected Output: (%d + %d) ^ 2 = %d" % (x, y, solve))