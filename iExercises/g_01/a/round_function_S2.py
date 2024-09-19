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

print("original number: ", x)
x = x + 0.5
a = str(x)
y = a.find(".")
print("Rounded off int: ", a[0:y])