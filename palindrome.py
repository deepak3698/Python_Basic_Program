

input_val=int(input("Enter a number :"))

another_var=input_val
sum=0
while(another_var!=0):
    sum=sum*10+another_var%10
    another_var=another_var//10


if(input_val==sum):
    print(f"The number {input_val} is a palindrome number.")
else:
    print(f"The number {input_val} is not a palindrome number.")