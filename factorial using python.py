def fact(num):
    if(num==0):
        return 1
    return num*fact(num-1)
x=int(input("enter a number"))
z=fact(x)
print(z)
