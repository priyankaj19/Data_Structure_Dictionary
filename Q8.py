# Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary.
string = input("Enter string: ")
dictionary = {} 
l = list(string.split())   # remove spaces
m = list(set(l))           # list without duplicates of words
for x in m:                # x is word
    y = l.count(x)         # y denotes frequency of word
    dictionary[x] = y  
print(dictionary)

# OR

string = input("Enter string: ")
dictionary = {} 
l = list(string.split())         # remove spaces
m = list(set(l))                 # list without duplicates of words
for x in m:                      # x is word
    dictionary[x] = l.count(x)   # count frequency of words
print(dictionary)