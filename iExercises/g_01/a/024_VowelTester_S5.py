# ----------------------------------------------------------------------------------
# - Write a Python program to test whether a passed letter is a vowel or not.
# ----------------------------------------------------------------------------------

# Using find()
def isVowel(ch):
  
  # Make the list of vowels
  str = "aeiouAEIOU"
  return (str.find(ch) != -1)

# Driver Code
print('a is '+str(isVowel('a')))
print('x is '+str(isVowel('x')))