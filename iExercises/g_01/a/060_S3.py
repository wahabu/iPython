# Write a Python program to calculate the hypotenuse of a right angled triangle.

# Define a function named 'test' that takes two parameters 'x' and 'y'.
def test(x, y):
    # Calculate the length of the hypotenuse (h) using the Pythagorean theorem.
    h = (x**2 + y**2)**0.5
    
    # Return the calculated hypotenuse.
    return h

# Call the 'test' function with different values and print the results.
# Calculate the hypotenuse for a right triangle with sides two numbers input from a user.
print(test(int(input("Input a number:")), int(input("Input a number:"))))