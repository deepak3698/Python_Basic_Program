'''program for reverse string '''


a =input("Enter your string")
b=""
leng=len(a)

for i in range(leng):
    b=b+a[leng-1-i]

print(b)