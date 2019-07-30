from functools import reduce

list_of_numbers_to_check=[5,20,15,10]

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

def get_lcm_for(list1):
    return reduce(lambda x, y: lcm(x, y), list1)

print(f"LCM of {list_of_numbers_to_check} will be {get_lcm_for(list_of_numbers_to_check)}")

