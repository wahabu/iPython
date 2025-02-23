# ----------------------------------------------------------------------------------------------
# - Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
# - Note: Do not use built-in functions.
# ----------------------------------------------------------------------------------------------


numbers = [4, 209, 17, 51, 26, 272]

def iMax(sequence_numbers):
    max = 0
    min = 0
    for x in sequence_numbers:
        max = x
        min = x
        for x in numbers:
            if x > max:
                max = x
            elif x < min:
                min = x

    return max, min

print(iMax(numbers))