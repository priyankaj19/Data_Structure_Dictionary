# Python Program to Sum All the Items in a Dictionary.
data={'a': 300, 'b':200, 'c':10, 'd':40, 'e':50}
sum_values = 0

for x in data.values():
    sum_values += x

print("Sum of values:",sum_values)

# OR
data={'a': 300, 'b':200, 'c':10, 'd':40, 'e':50}
sum_values = 0

for x in data:
    sum_values += data[x]

print("Sum of Values:",sum_values)

# OR
data={'a': 300, 'b':200, 'c':10, 'd':40, 'e':50}
print("The Sum of Values: ", sum(data.values()))