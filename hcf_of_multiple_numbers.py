from functools import reduce

def find_hcf(n1,n2):
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
    return hcf


def get_hcf_for(list_of_numbers_for_hcf):
    return reduce(lambda x, y: find_hcf(x, y), list_of_numbers_for_hcf)


list_of_numbers_for_hcf=[4,6,8,10]

print(f"HCF of {list_of_numbers_for_hcf} will be {get_hcf_for(list_of_numbers_for_hcf)}")