f=open("myfile.txt","w")
print("enter the text # when done")
s=''
while s!='#':
   s=input()
   f.write(s)


f.close()