# -----------------------------------------------------------------------------
# -- Write a Python program that accepts an integer (n) and computes ----------
# -- the value of n+nn+nnn. ---------------------------------------------------
# -- Sample value of n is 5 ---------------------------------------------------
# -- Expected Result: 615 -----------------------------------------------------
# -----------------------------------------------------------------------------

# Prompt the user to enter a number and store it as a string in variable 'n'
n = input("Enter any number: ")

# Print the type of 'n' to verify it is a string (for debugging purposes)
print(type(n))

# Initialize an empty list to store string representations of the number
list = []

# Loop to generate the string representations n, nn, and nnn
for i in range(3):
    # For i == 0, append 'n' to the list
    if (i == 0):
        list.append(n)
    # For i == 1, append 'n' and then concatenate it with itself (i.e., nn)
    if (i == 1):
        list.append(n)
        list[i] = list[i] + list[i]
    # For i == 2, append 'n' and then concatenate it twice more (i.e., nnn)
    if (i == 2):
        list.append(n)
        list[i] = list[i] + list[i] + list[i]

# Print the list for debugging purposes (commented out)
#print(list)

# Convert each string in the list to an integer, sum them up, and print the result
print("Result: ", int(list[0]) + int(list[1]) + int(list[2]))