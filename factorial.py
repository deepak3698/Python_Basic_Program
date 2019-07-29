

input_val=int(input("Enter a number :"))
factorial=1

for i in range(2,input_val+1):
    factorial=factorial*i

print(f"The factorial of {input_val} is {factorial}.")