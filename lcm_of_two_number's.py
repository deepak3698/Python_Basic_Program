
def lcm(x,y):
    for i in range(1,x*y+1):
        if(i%x==0 and i%y==0):
            break
    return i

n1=int(input("Enter your First Number :"))
n2=int(input("Enter your Second Number :"))

print(f"LCM of {n1} and {n2} will be {lcm(n1,n2)}")