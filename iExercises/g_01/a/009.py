# -----------------------------------------------------------------------------
# -- Write a Python program to display the examination schedule. --------------
# -- (extract the date from exam_st_date). ------------------------------------
# -- exam_st_date = (11, 12, 2014) --------------------------------------------
# -- Sample Output: The examination will start from: 11 / 12 / 2014 -----------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

# Define a variable that contains the exam date as a tuple
exam_st_date = (11, 12, 2014)

# Use join to combine the elements into a string, converting each element to a string
formatted_date = " / ".join(map(str, exam_st_date))

# Print the final result with the formatted date
print(f"The examination will start from: {formatted_date}")
