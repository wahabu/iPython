# ----------------------------------------------------------------------------------------
# - Write a Python program to round numbers without using the built-in round() function.
# ----------------------------------------------------------------------------------------
# # # # # # # # # # # # # # #
# Pictorial Presentation:   #
#  round(11.5)              #
#        ||                 #
#      \    /               #
#       \  /                #
#        \/                 #
#        11.5               #
#          ||               #
#        \    /             #
#         \  /              #
#          \/               #
#        5 >= 5             #
#        \    /             #
#         \  /              #
#          \/               #
#      11 + 1 = 12          #
#             \    /        #
#              \  /         #
#               \/          #
#               12          #
# # # # # # # # # # # # # # #

x = float(input("Input a float number: "))

result = int(x-0.5)+1
print(x-0.5+1)
print(result)

result_10 = (int(10*x-0.5)+1) / 10.0

print(result_10)