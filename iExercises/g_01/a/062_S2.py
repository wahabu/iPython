# - Write a Python program to convert all units of time into seconds.
# ---------------------------------------------------------------------

# Prompt the user to input a number a number of days and store it in the variable 'days'.
days = int(input("Input days: ")) * 3600 * 24

# Prompt the user to input a number of hours and store it in the variable 'hours'.
hours = int(input("Input hours: ")) * 3600

# Prompt the user to input a number of minutes and store it in the variable 'minutes'.
minutes = int(input("Input minutes: ")) * 60

# Prompt the user to input a number of seconds and store it in the variable 'seconds'.
seconds = int(input("Input seconds: "))

# Calculate the total time in seconds by adding the converted values.
time = days + hours + minutes + seconds

# Print the total time in seconds.
print("The amount of seconds: ", time)