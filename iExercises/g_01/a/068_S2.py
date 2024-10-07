# Write a Python program to calculate sum of digits of a number.

# Prompt the user to input a four-digit number and convert it to an integer.
num = int(input("Input a four-digit number: "))

# Extract the thousands digit (x).
x = num // 1000 # 

# Extract the thousands digit (x1) by subtracting the thousands digit from the number.
x1 = (num - x * 1000) // 100