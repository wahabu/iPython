# ----------------------------------------------------------------------------------------------
# - Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
# - Note: Do not use built-in functions.
# ----------------------------------------------------------------------------------------------

# Define a function named 'max_min' that takes a list 'data' as its argument.
def max_min(data):
    # Initialize two variables 'l' and 's' with the first element of the 'data' list.
    l = data[0] # 'l' is used to keep track of the maximum value.
    s = data[0] # 's' is used to keep track of the minimum value.
    
    # Iterate through each number 'num' in the 'data' list.
    for num in data:
        # Check if the current number 'num' is greater than the current maximum 'l'.
        if num > l:
            l = num # If 'num' is greater, update 'l' with 'num'.
        # Check if the current number 'num' is smaller than the current minimum 's'.
        elif num < s:
            s = num # If 'num' is smaller, update 's' with 'num'.

    # Return the maximum 'l' and minimum 's' values as a tuple.
    return l, s

# Call the 'max_min' function with a list of numbers and print the result.
print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))