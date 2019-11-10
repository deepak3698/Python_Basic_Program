### program for  prime number upto user input
from math import *
n=int(input("Enter a number "))
for j in range(2,n+1):
    for i in range(2,floor(sqrt(j))+1):
        if(j%i==0):
            break
    else:
        print(j)