
f=open("word_data","r")

for i in f:
    data=i.rstrip("\n").split(" ")
    print(data)

dic={}

print(data)
for i in data:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)