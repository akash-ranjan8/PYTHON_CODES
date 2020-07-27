import re
s = input("enter a string")
result=re.search(r'o\d\d',s)
print(result.group())