# ------------------------------------------------------------------------------
# - Write a Python program whether a passed letter is a vowel or not.
# ------------------------------------------------------------------------------

# Function to check whether a character
# is vowel or not
def vowelOrConsonant(x):
  
  if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
    print("Vowel")
  else:
    print("Consonant")
    
# Driver code
vowelOrConsonant('c')
vowelOrConsonant('e')