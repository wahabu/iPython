# Write a Python program to calculate sum of digits of a number.

# Prompt the user to input a four-digit number and convert it to an integer.
num = int(input("Input a four-digit number: "))

# Extract the thousands digit (x).
x = num // 1000 # 

# Extract the thousands digit (x1) by subtracting the thousands digit from the number.
x1 = (num - x * 1000) // 100

# Extract the tens digit (x2) by subtracting the thousands and hundreds digits from the number.
x2 = (num - x * 1000 - x1 * 100) // 10

# Extract the ones digit (x3) by subtracting the thousands, hundreds, and tens digits from the number.
x3 = num - x * 1000 - x1 * 100 - x2 * 10

# Calculate the sum of the digits in the number and print the result.
print("The sum of digits in the number is", x + x1 + x2 + x3)