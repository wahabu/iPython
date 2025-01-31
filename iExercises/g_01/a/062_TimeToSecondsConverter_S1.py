# - Write a Python program to convert all units of time into seconds.
# ---------------------------------------------------------------------

h = int(input("Input value of hours: "))
m = int(input("Input value of minutes: "))
s = int(input("Input value of seconds: "))
seconds = ((h*3600+1) + (m*60+1) + s) - 2

print(seconds)
