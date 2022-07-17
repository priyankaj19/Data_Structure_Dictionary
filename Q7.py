# Python Program to Remove the Given Key from a Dictionary.
data={'a': 300, 'b':200, 'c':10, 'd':40, 'e':50}
key = input("Enter key to remove: ")
print("Original data: ",data)
data.pop(key)     # remove pair of key+value
print("Updated data: ",data)

# OR
data={'a': 300, 'b':200, 'c':10, 'd':40, 'e':50}
key = input("Enter key to remove: ")
print("Original data: ",data)
del data[key]      # remove pair of key+value
print("Updated data: ",data)