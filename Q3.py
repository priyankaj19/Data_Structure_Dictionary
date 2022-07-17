# Python Program to Check if a Given Key Exists in a Dictionary or Not.
data = {101:'God' , 102:'piya' , 103: 'namu', 104: 'shubh'}
key=int(input("Enter key from data: "))

if key in data:
    print("Key is present.")
else:
    print("Key is not present.")