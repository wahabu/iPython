# ---------------------------------------------------------------------------------
# - Write a Python program to convert height (in feet and inches) to centimeters.
# ---------------------------------------------------------------------------------

def h_ft_and_in(h_ft, h_in):
    cm_ft = 30.48 * float(h_ft)
    cm_in = 2.54 * float(h_in)
    total = cm_in + cm_ft
    height_cm = int(cm_in + cm_ft)
    if total - height_cm >= 0.5:
        return height_cm + 1
    else:
        return height_cm

h_ft = input("Input the feet value: ") # 5
h_in = input("Input the inch value: ")# 9+11/16
print(h_ft_and_in(h_ft, h_in))