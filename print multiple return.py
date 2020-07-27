def calculator(a,b):
    x=a+b
    y=a-b
    z=a*b
    w=a/b
    return x,y,z,w 
c=int(input("enter first no."))
d=int(input("enter second no."))
r=calculator(c,d)
print(r)