# Python Program to Generate a Dictionary that Contains Numbers 
# (between 1 and n) in the Form (x,x*x).

data={}
n=int(input("Enter a number:"))

for i in range(1,n+1):
    data[i]=(i,i*i)
print(data)