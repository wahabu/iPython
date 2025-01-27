# Write a Python program to sum the first n positive integers.

# Prompt the user for input and convert it to an integer.
n = int(input("Input a number: "))

# s_n = sum of the consecutive integers
# n = number of integers
# a = first term
a = 1
# l = last term
l = n

# Calculate the sum of the first 'n' positive integers using the formula.
s_n = n * (a + l) / 2

# Print the result, indicating the sum of the first 'n' positive integers.
print("Sum of the first", n, "postive integers: ", s_n)