def lcm(x,y):
    if (x > y):
        big_num = x
    else:
        big_num = y
    check_for=0
    i=1
    while(check_for!=x*y):
        check_for = big_num * i
        if (check_for % x == 0 and check_for % y == 0):
            break
        i=i+1

    return check_for

n1=int(input("Enter your First Number :"))
n2=int(input("Enter your Second Number :"))

print(f"LCM of {n1} and {n2} will be {lcm(n1,n2)}")