'''lst=[10,15,20,30,35,40,45,50,55,60,65,70]

print(lst)

for i in lst:
    print(i)

sum=0

for i in lst:
    sum+=i
print(sum)


print(max(lst))

print(min(lst))

print(len(lst))'''


#....................................................


'''lst=[4,1,6,50,34,21,50,63,21,43,20,31,47]

for i in lst:
    if i%2==0:
        print(i)
'''

'''sum=0


lst=[]

lst.append(150)

print(lst)'''

'''lst=[]
even_lst=[]
odd_lst=[]

print(lst)

for i in range(1,100):
    lst.append(i)
print(lst)

for i in lst:
    if i%2==0:
        even_lst.append(i)
    else:
        odd_lst.append(i)

print(even_lst)
print(odd_lst)
print(sum(lst))'''


# remove a value


# remove :- function



'''lst=[30,35,10,15,20,100,75,32]
lst.remove(35)

print(lst)'''

# pop :- funtions

lst=[30,35,10,15,20,100,75,32]

lst.pop(3)
print(lst)