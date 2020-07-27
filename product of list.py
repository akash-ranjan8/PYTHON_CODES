lst=[int(x) for x in input("enter numbers").split()]
prod=1
for i in lst:
    prod*=i
    print(prod)
print("the product is:",prod)
