flag=True
x=int(input("enter a number"))
for i in range(2,x-1):
    if(x%i==0):
        flag=False
if(flag==True):
    print("prime")
else:
    print("not prime")
    
    