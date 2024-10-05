# Write a Python programe that finds and displays all prime numbers from 1 to 20.

# Initialize an empty list to hold natural numbers from 1 to 20.
natural_numbers = []

# Initialize an empty list to store prime numbers extracted from the natural_numbers list.
prime_numbers = []

# Initialize a counter variable for generating natural numbers.
i = 1

# Use a while loop to populate the list with natural numbers from 1 to 20.
while i < 21:
    natural_numbers += [i]
    i += 1

# Iterate over each number in natural_numbers to determine how many divisors it has.
for i in natural_numbers:
    # Initialize a counter to track the number of divisors for the current number.
    count = 0
    
    # Iterate over natural_numbers to check if 'j' is a divisor of 'i'.
    for j in natural_numbers:
        # Check if 'i' is divisible by 'j'; if so, increment the divisor count.
        if i % j == 0:
            count +=1
    
    # If the number has exactly two divisors (1 and itself), it is prime; add it to prime_numbers.
    if count == 2:
        # Add the number to the list of prime numbers.
        prime_numbers += [i]
            
# Display the list of natural numbers.
print(natural_numbers)
# Display the list of prime numbers.
print(prime_numbers)