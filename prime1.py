
input_val=int(input("Enter a Number :"))

for i in range(2,input_val+1):
    if(input_val%i==0):
        break

if(input_val==i):
    print(f"The number {input_val} is a prime number !")
else:
    print(f"The number {input_val} is not a prime number !")
