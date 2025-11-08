data="hai hello hai hello hai hello hai hai"

print(data)

# hai==5
# hello==3


#  1) split

words=data.split(' ')
print(words)


dic={}

'''print("hai" in dic)

dic["hai"]=1

print("hello" in dic)

dic["hello"]=1

print(dic)

print("hai" in dic)

dic["hai"]+=1

print(dic)

print("hello" in dic)

dic["hello"]+=1

print("hai" in dic)

dic["hai"]+=1

print("hello" in dic)

dic["hello"]+=1

print("hai" in dic)

dic["hai"]+=1

print("hai" in dic)

dic["hai"]+=1

print(dic)'''

for i in words:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)


