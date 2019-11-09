
from functools import reduce

def hcf(a,b):
    for i in range(min(a,b),0,-1):
        if(a%i==0 and b%i==0):
            break
    return i

def get_hcf_for(list_of_numbers_for_hcf):
    return reduce(lambda x, y: hcf(x, y), list_of_numbers_for_hcf)

list1=[6,18,24,12]
print(f" HCF of Given Number's will be {get_hcf_for(list1)}.")
