# - Write a Python program to convert the distance (in feet) to inches, yards, and miles.
# -----------------------------------------------------------------------------------------

distance_ft = int(input("Input a distance: "))

distance_in = 12 * distance_ft
distance_yd = 0.333333 * distance_ft
distance_mi = 0.000189394 * distance_ft

print(distance_in)
print(distance_yd)
print(distance_mi)