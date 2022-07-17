# Python Program to Multiply All the Items in a Dictionary.
data={'a': 300, 'b':200, 'c':10, 'd':40, 'e':50}
mul_values = 1

for x in data.values():
    mul_values *= x

print("Multiplication of values:",mul_values)

# OR
data={'a': 300, 'b':200, 'c':10, 'd':40, 'e':50}
mul_values = 1

for x in data:
    mul_values *= data[x]

print("Multiplication of Values:",mul_values)