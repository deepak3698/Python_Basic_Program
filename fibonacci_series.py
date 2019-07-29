

# fibanacci series: 0,1,1,2,3,5,8,13,21,34


input_value=int(input("Enter a number :"))
prev=0
nextt=1
print(f"The fibonacci series upto {input_value} is {prev} {nextt} ",end="")
for i in range(1,input_value-1):
    a=prev+nextt
    print(a,end=" ")
    prev=nextt
    nextt=a
   
