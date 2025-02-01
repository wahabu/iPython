# - Write a Python program that converts seconds into days, hours, minutes, and seconds.
# ----------------------------------------------------------------------------------------

# - Prompt the user to inoput a time duration in seconds and convert it to a float.
time = float(input("Input time in seconds: "))

# Calculate the number of full days in the given time duration.
day = time // (24 * 3600)
# Update the time variable to hold the remaining seconds after subtracting full days.
time = time % (24 * 3600)

# Calculate the number of full hours in the remaining time.
hour = time // 3600
# Update the time variable to hold the remaining seconds after subtracting full hours.
time %= 3600

# Calculate the number of full minutes in the remaining time.
minutes = time // 60
# Update the time variable to hold the remaining seconds after subtracting full minutes.
time %= 60

# The 'time' variable now represents the remaining seconds, which is the number of seconds.
seconds = time

# Print the time duration in the format "d:h:m:s".
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))