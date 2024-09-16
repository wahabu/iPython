#############################################################################################
# The range() function is used to get a sequence of numbers, starting from 0 by default, and increments by 1 by default, and ends at a specified number.

# Note Sequence Types - list, tuple, range etc.

# range(start, stop, [step])

# empty range
print(list(range(0))) # Output: []

# using range(stop)
print(list(range(10))) # Output: [0, 1... , 9]

# using range(start, stop)
print(list(range(3, 10))) # Output: [3, 4... , 9]

# using range(start, stop, [step])
print(list(range(1, 15, 3))) # Output: [1, 4, 7, 10, 13]

# range() works with negative step
print(list(range(0, -10, -1))) # Output: [0, -1, -2... , -9]