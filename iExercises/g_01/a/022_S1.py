# ----------------------------------------------------------------
# - Write a Python program to count hte number 4 in a given list.
# ----------------------------------------------------------------

# Declaring a list
list_numbers = [22, 4, 1, 8, 4, 1, 20, 15, 11, 4, 9, 0, 44, 4, 10, 4]

# Using sum with a generator expression to count the number 4
count = sum(1 for i in list_numbers if i == 4)

print(count)