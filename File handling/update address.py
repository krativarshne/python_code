#to update and edit address
f=open("filename.txt",'r+')
str=f.read()
print(str)
str1=input()
f.write(str1)
print("Updated Address Is")
print(str1)
f.close()
