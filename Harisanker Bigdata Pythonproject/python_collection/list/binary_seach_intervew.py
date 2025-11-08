'''for x in range(2,11,3):
    print(x,end="")
    if x==3:
        break
    else:
        x=x+1
else:
    print("error")'''



'''lst=[6,5,4,3,2,1]


lst.sort()
print(lst)

low=0
upp=len(lst)-1

element=int(input("enter a number"))

while (low<=upp):
    res=lst[low]+lst[upp]

    if (res==element):
        print(lst[low],lst[upp])
        
    elif (res>element):
        upp=upp-1
    else:
        low=low+1'''






lst=[4,8,12,10]

lst1=[]

sum=sum(lst)

for i in lst:
    lst1.append(sum-i)

print(lst1)

