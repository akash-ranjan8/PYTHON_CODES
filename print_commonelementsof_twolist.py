a=[1,2,3,4,5]
b=[2,7,8,5,10]
z=[]
for i in a:
    if i in b:
        z.append(i)
print(z)