
dict1={1:0,2:1}

input_value=int(input("Enter a number :"))
prev=0
nextt=1
print(f"The fibonacci series upto {input_value} is {prev} {nextt} ",end="")
for i in range(1,input_value-1):
    a=prev+nextt
    print(a,end=" ")
    dict1[i+2]=a
    prev=nextt
    nextt=a
   
print()
print(f"Fibonacci series in dictionary is {dict1}")