# Write a program that simulates a coffee machine. The machine should have a list of available coffee options (e.g., "Cappuccino" and "Espresso"). It should be able to make a coffee when a valid coffee type is provided and return a message stating the coffee type that was made. If an invalid coffee type is requested, the machine should return a message indicating that the option is not valid. Implement this behavior in a [CoffeeMachine] class and create a method [make_coffee] to handle the coffee-making process. Demonstrate the functionality by trying both valid and invalid coffee options.

class CoffeeMachine:
    def __init__(self):
        self.coffee_options = {"Capuccino", "Espresso"}
        
    def make_coffee(self, coffee_type):
        is_valid_coffee_type = coffee_type in self.coffee_options
        if is_valid_coffee_type:
            return f"{coffee_type} made!"
        else:
            return f"{coffee_type} is not a valid option!"

machine = CoffeeMachine()
print(machine.make_coffee("Espresso"))
print(machine.make_coffee("Moka"))