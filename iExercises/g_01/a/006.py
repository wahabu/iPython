# -----------------------------------------------------------------------------
# -- Program that accepts a sequence of comma-seprated numbers from the user --
# -- and generates a list and a tuple of those numbers ------------------------
# -- Sample data: 3, 5, 7, 23 -------------------------------------------------
# -- Output: ------------------------------------------------------------------
# -- List: ['3', '5', '7', '23'] ----------------------------------------------
# -- Tuple: ('3', '5', '7', '23')

lSequence = int(input("Enter the length sequence:"))

numbers = []
a = 0
while a < lSequence:
   numbers.append(input())
   a = a+1
print(numbers)
listToTuple = tuple(numbers)
print(listToTuple)
print(type(numbers))
print(type(listToTuple))
