input_val=int(input("Enter binary value !"))

n=input_val
sum=0
i=0
while(n!=0):
    sum=sum+(n%10)*(2**i)
    n=n//10
    i=i+1

print(f"The decimal number of {input_val} will be {sum} ")