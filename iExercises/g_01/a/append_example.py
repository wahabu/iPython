# Write a Python program that uses the append() method to add elements to a list.
# This program demonstrates how individual elements are added to the end of the list.

# Initialize an empty list
list_items = []

# Add elements to the list using append()
list_items.append(1)
print(list_items) # Output: [1]

list_items.append(2)
print(list_items) # Output: [1, 2]

list_items.append([3, 4])
print(list_items) # Output: [1, 2, [3, 4]] # The entire list is added as a single element.