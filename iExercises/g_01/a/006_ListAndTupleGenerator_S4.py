# -----------------------------------------------------------------------------
# -- Program that accepts a sequence of comma-seprated numbers from the user --
# -- and generates a list and a tuple of those numbers ------------------------
# -- Sample data: 3, 5, 7, 23 -------------------------------------------------
# -- Output: ------------------------------------------------------------------
# -- List: ['3', '5', '7', '23'] ----------------------------------------------
# -- Tuple: ('3', '5', '7', '23')

# Prompt the user to enter the length of the sequence (number of values to input) and convert it to an integer
values = int(input("Enter the length of the sequence:"))

# Initialize an empty list to store the user inputs
numbers = []

# Initialize a counter variable 'a' to 0
a = 0

# Start a while loop that runs until 'a' is less than 'values_02'
while a < values:
   # Prompt the user for input, strip any leading/trailing spaces, and append the value to the 'numbers' list
   numbers.append(input().strip())
   
   # Increment the counter 'a' by 1 in each iteration
   a = a + 1

# Print the 'numbers' list containing all the user inputs
print(numbers)

# Convert the 'numbers' list into a tuple and store it in 'listToTuple'
listToTuple = tuple(numbers)

# Print the 'listToTuple' tuple
print(listToTuple)

# Print the type of the 'numbers' variable (which is a list)
print(type(numbers))

# Print the type of the 'listToTuple' variable (which is a tuple)
print(type(listToTuple))
