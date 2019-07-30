n1=int(input("enter your first number !"))
n2=int(input("enter your second number !"))
list1=[]
hcf=0
if(n1>n2):
    small=n2
    big=n1
else:
    small=n1
    big=n2

if(big%small==0):
        hcf=small
else:
    for i in range(2,small+1):
        if(small%i==0):
            list1.append(i)
    for i in range(len(list1)):
        if(big%list1[i]==0):
            hcf=list1[i]

print(f"HCF of {n1} and {n2} is {hcf}")