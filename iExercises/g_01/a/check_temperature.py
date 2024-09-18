# Write a Python program to check the water temperature. If temperature is above 30, return True.
# Otherwise, return False.

def can_swim(temperature):
  if temperature < 30:
    return True
  else:
    return False
  
print(can_swim(31))