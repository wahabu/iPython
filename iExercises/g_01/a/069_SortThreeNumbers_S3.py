# Read three integers
a = int(input())
b = int(input())
c = int(input())

# Compute the maximum of a and b
max_ab = a * (a >= b) + b * (b > a)
# Compute the maximum of max_ab and c
max_abc = max_ab * (max_ab >= c) + c * (c > max_ab)

# Compute the minimum of a and b
min_ab = a * (a <= b) + b * (b < a)
# Compute the minimum of min_ab and c
min_abc = min_ab * (min_ab <= c) + c * (c < min_ab)

# Compute the median value
median = a + b + c - max_abc - min_abc

# Print the sorted integers
print(min_abc, median, max_abc)
