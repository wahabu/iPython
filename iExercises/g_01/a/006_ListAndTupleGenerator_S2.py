# -----------------------------------------------------------------------------
# -- Program that accepts a sequence of comma-seprated numbers from the user --
# -- and generates a list and a tuple of those numbers ------------------------
# -- Sample data: 3, 5, 7, 23 -------------------------------------------------
# -- Output: ------------------------------------------------------------------
# -- List: ['3', '5', '7', '23'] ----------------------------------------------
# -- Tuple: ('3', '5', '7', '23')

# Prompt the user to input a sequence of comma-separated numbers and store it in the 'values' variable
values = input("Enter some comma-separated numbers: ")

# Split the 'values' string into a list using commas as separators and strip spaces from each element
values_list = [x.strip() for x in values.split(",")]

# Convert the 'values_list' into a tuple
values_tuple = tuple(values_list)

# Print the list
print('List: ', values_list)

# Print the tuple
print('Tuple : ', values_tuple)