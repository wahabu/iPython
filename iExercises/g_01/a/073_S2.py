# Write a Python program to calculate the midpoints of a line.

# Print a message to inform the user that the program will calculate the midpoint of a line.
print('\nCalculate the midpoint of a line: ')

# Prompt the user to enter the x and y coordinates of the first endpoint of the line.
x1 = float(input())
y1 = float(input())

# Prompt the user to enter the x and y coordinates of the second endpoint of the line.
x2 = float(input('The value of x (the first endpoint)'))
y2 = float(input('The value fo y (the first endpoint)'))

# Calculate the x-coordinate of the midpoint of the line.
x_m_point = (x1 + x2) / 2

# Calculate the y-coordinate of the midpoint of the line.
y_m_point = (y1 + y2) / 2
print();

