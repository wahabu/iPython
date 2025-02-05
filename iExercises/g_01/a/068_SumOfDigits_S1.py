# Write a Python program to calculate sum of digits of a number.

x = int(input("Input a number: "))
sum = 0
for i in str(x):
    sum += int(i)
    
print(sum)