
input_val=int(input("Enter Decimal number !"))

n=input_val
sum=""
while(n//2!=0):
    sum=str(sum)+str(n%2)
    n=n//2
sum='1'+sum[::-1]

print(f"The binary value of {input_val} will be {sum} ")



