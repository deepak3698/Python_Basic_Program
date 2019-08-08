######## Program for Reverse Number #########

input_val=int(input("Enter a number: "))
check=input_val
sum=0
while(check!=0):
    r=check%10
    sum=sum*10+r
    check=check//10
print(f"Reverse of the number {input_val} is {sum}")