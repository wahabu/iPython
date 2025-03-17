# Write a Python program that returns a string that is n (non-negative integer) copies of a given string.

# Define a function named "larger_string" that takes two parameters, "text" and "n"
def larger_string(text, n):
    # Initialize an empty string variable named "result"
    result = ""

    # Use a for loop to repeat the "text" "n" times and concatenate it to the "result"
    for i in range(n):
        result = result + text

    # Return the final "result" string
    return result

# Call the "larger_string" function with the arguments 'abc' and 2, then print the result
print(larger_string('abc', 2))

# Call the "larger_string" function with the arguments '.py' and 3, then print the result
print(larger_string('.py', 3))
