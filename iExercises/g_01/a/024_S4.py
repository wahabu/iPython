# ------------------------------------------------------------------------------------
# - Write a Python program to test whether a passed letter is a vowel or not.
# ------------------------------------------------------------------------------------

# Useing switch case
def isVowel(ch):
  switcher = {
    'a': "Vowel",
    'e': "Vowel",
    'i': "Vowel",
    'o': "Vowel",
    'u': "Vowel",
    'A': "Vowel",
    'E': "Vowel",
    'I': "Vowel",
    'O': "Vowel",
    'U': "Vowel",
  }
  return switcher.get(ch, "Consonant")

# Driver Code
print('a is '+isVowel('a'))
print('x is '+isVowel('x'))