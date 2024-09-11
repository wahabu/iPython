# -----------------------------------------------------------------------
# - Write a Python program to whether a passed letter is a vowel or not.
# -----------------------------------------------------------------------

# Define a function called letter_check that takes one parameter: char (a character).
def letter_check(letter):
  # List of vowel letters
  vowel_letters = ["a", "e", "i", "o", "u"]
  is_vowel = False # Variable to track if the letter is a vowel
  
  # Check each letter in the vowel list
  for i in vowel_letters:
    if letter == i:
      is_vowel = True # Update the variable to True if the letter is a vowel
      
  # Print the appropriate message based on whether a vowel was found
  if is_vowel:
    print("Vowel letter")
  else:
    print("Normal letter")
    
# Prompt the user to enter a letter
letter = input("Enter a letter: ")
letter_check(letter)