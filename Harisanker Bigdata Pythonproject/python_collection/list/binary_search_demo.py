'''lst=[10,20,30,40,50,60,70,80,90,100]

lst.sort()
print(lst)

low=0
upper=len(lst)-1

flag=0

element=int(input("enter a element"))

while (low<=upper):
    mid = (low + upper) // 2

    if (element>lst[mid]):
        low=mid+1

    elif (element<lst[mid]):
        upper=mid-1

    elif (element==lst[mid]):

        flag=1
        break

if(flag>0):
    print("element found")
else:
    print("element not found")
'''

#.............................................................



lst=[1,3,5,7,8,4,3,2,1,5,6,8,9,2,1,4,6,7,6,5,4,3]

# collect :- 1,8,1,9,1,7

'''lst.sort()
print(lst)'''

# whenever a seres is increased or decreased

