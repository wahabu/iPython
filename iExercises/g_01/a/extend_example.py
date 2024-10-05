# Write a Python program that uses the extend() method to add multiple elements to a list.
# This program demonstrates how a list can be extended with another list of elements.

# Initialize an empty list
list_items = []

# Add elements to the list using extend()
list_items.extend([1, 2])
print(list_items) # Outpus: [1, 2]

list_items.extend([3, 4])
print(list_items) # Output: [1, 2, 3, 4] # Each element in the list is added individually.

list_items.extend([5, 6])
print(list_items) # Output: [1, 2, 3, 4, 5, 6] # The elements of the list are appended one by one.