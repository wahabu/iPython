# Python lists
# A Python list is a collection of ordered items that can hold elements of different types. Lists are mutable, meaning their contents can be modified after creation.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Lists: Commands
numbers.append(10) # <list>.append(<el>)
print(numbers) # >> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Or
numbers += [11] # <list> += [11]
print(numbers) # >> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

letters = ["A","B","C"]

letters.extend("cba") # <list>.extend(<collection>)
print(letters) # >> ['A', 'B', 'C', 'c', 'b', 'a']
# Or
numbers += 12, 13 # <list> += <collection>
print(numbers) # >> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

letters.sort() # <list>.sort()
print(letters) # >> ['A', 'B', 'C', 'a', 'b', 'c']

numbers = [1, 2, 3, 6, 1, 2, 3, 4, 6, 12]
numbers.sort() # <list>.sort()
print(numbers) # >> [1, 1, 2, 2, 3, 3, 4, 6, 6, 12]

numbers.reverse() # <list>.reverse()
print(numbers) # >> [12, 6, 6, 4, 3, 3, 2, 2, 1, 1]

letters = []
letters = sorted('badec') # <list> = sorted(<collection>)
print(letters) # >> ['a', 'b', 'c', 'd', 'e']

numbers = [10, 20, 30, 40, 50, 60]
iterator = reversed(numbers) # <iter> = reversed(<list>)
print(list(iterator)) # >> [60, 50, 40, 30, 20, 10]