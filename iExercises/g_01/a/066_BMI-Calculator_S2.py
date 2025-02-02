# Write a Python program to calculate the body mass index.

# Prompt the user to input their height in feet and convert it to a floating-point number.
height = float(input("Input your height in Feet: "))

# Prompt the user to input their weight in lilograms and convert it to a floating-point number.
weight = float(input("Input your weight in Kilograms: "))

# Calculate the body mass index (BMI) using the provided height and weight and round it to 2 decimal places.
bmi = weight / (height * height)
rounded_bmi = round(bmi, 2)

# Print the calculated BMI.
print("Your body mass index is: ", rounded_bmi)