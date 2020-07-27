try:
    num=int(input("enter a even no."))
    assert num%2==0,"entered an invalid number"
except AssertionError as obj:
    print(obj)
print("after assertion")
