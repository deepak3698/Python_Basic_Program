

list_of_prime_numbers=[]
input_val=int(input("Enter Your Number :"))

for i in range(2,input_val+1):
    for j in range(2,i+1):
        if(i%j==0):
            break
    if(i==j):
        list_of_prime_numbers.append(j)
    else:
        pass
print(f"Prime numbers are upto {input_val} {list_of_prime_numbers}.")
        