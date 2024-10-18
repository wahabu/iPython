# There's a cafe nearby that offers a new variety of beverages every day. We have a Beverage class and two instances: fruity and cocoa. Find out what's in today's drinks.

# Tasks:

# Access the name property of the fruity beverage and print it to the console.
# Access the is_alcoholic property of the cocoa beverage and print it to the console.

class Beverage:
    def __init__(self, name, is_alcoholic):
        self.name = name
        self.is_alcoholic = is_alcoholic

fruity = Beverage("Fruit punch", False)
cocoa = Beverage("Hot chocolate", False)
print(fruity.name)
print(cocoa.is_alcoholic)