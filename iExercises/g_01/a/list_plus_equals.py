# Write a Python program that creates an empty list, adds elements to it one by one, and prints the list after each addition.

list_items = []
print(list_items) # >> []
list_items += [1]
print(list_items) # >> [1]
list_items += [3]
print(list_items) # >> [1, 3]
list_items += [2]
print(list_items) # >> [1, 3, 2]

list_items2 = [5, 7, 9]
list_items += list_items2
print(list_items) # >> [1, 3, 2, 5, 7, 9]