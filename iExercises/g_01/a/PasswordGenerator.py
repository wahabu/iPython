import string
from random import *

letters = string.ascii_letters 
digits = string.digits 
symbols = string.punctuation
chars = letters + digits + symbols

min_length = 20
max_length = 25
password = "".join(choice(chars) for x in range(randint(min_length, max_length)))
print(password)