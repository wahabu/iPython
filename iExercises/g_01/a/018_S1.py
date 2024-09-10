# -----------------------------------------------------------------------------
# -- Write a Python program to calculate the sum of three given numbers.
# -- If the values are equal, return three times their sum.
# -----------------------------------------------------------------------------

num1 = int(input("Input the first number: "))
num2 = int(input("Input the second number: "))
num3 = int(input("Input the third number: "))

print("The total is: ", num1 + num2 + num3)

if (num1 == num2 == num3):
  print("The total is: ", (num1 + num2 + num3) * 3)
else:
  print("The of each number not equal.")