

input_val=int(input("Enter a number :"))

another_var=input_val
sum=0
while(another_var!=0):
    sum=sum+(another_var%10)**3
    another_var=another_var//10

if(input_val==sum):
    print(f"The number {input_val} is a armstrong number.")
else:
    print(f"The number {input_val} is not a armstrong number.")