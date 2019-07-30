from functools import reduce

list_of_numbers_to_check=[5,20,15,10]

def lcm(x,y):
    for i in range(1,x*y+1):
        if(i%x==0 and i%y==0):
            break
    return i

def get_lcm_for(list1):
    return reduce(lambda x, y: lcm(x, y), list1)

print(f"LCM of {list_of_numbers_to_check} will be {get_lcm_for(list_of_numbers_to_check)}")

