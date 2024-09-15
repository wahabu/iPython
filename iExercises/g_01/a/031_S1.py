# ---------------------------------------------------------------------------------------------------
# - Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
# ---------------------------------------------------------------------------------------------------

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a secound number: "))

list_1 = []
list_2 = []
greatest_common_divisor = []

count = 1
while (count <= num1):
  if (num1 % count == 0):
    list_1.append(count)
  count = count + 1

count = 1
while (count <= num2):
  if (num2 % count == 0):
    list_2.append(count)
  count = count + 1

greatest_common_divisor = [item for item in list_1 if item in list_2]
  
print(list_1)
print(list_2)
# print(max(list_2))
# print(max(list_1))
print(max(greatest_common_divisor))