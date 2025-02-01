# - Write a Python program that converts seconds into days, hours, minutes, and seconds.
# ---------------------------------------------------------------------------------------

seconds = int(input("Input seconds: "))
d = seconds // (24 * 3600)
h = (seconds % (24 * 3600)) // 3600
m = (seconds % 3600) // 60
s = (seconds % 60)

print(f"{d} days {h} hours {m} minutes {s} seconds")