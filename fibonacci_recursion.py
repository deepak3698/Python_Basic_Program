import time 

def fibonacci(n):
   if(n==1):
       return 0
   elif(n==2):
       return 1
   else:
       return fibonacci(n-1)+fibonacci(n-2)

n=int(input("Enter position of the Fibonacci series :"))

print(f" at {n} position the fibonacci value is {fibonacci(n)}.")