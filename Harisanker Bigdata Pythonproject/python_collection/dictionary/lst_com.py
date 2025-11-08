# create a empty list and add 1 to 75 numbers in it

lst=[]

for i in range(1,76):
    lst.append(i)

print(lst)

# reduce :- list comprehention

#    syntax

#  [print range]  #  print :- print statement

lst1=[i for i in range(1,76)]
print(lst1)


lst2=[3,4,5,6,7,8,9,10]

lst3=[i**2 for i in lst2]
print(lst3)

# lst4=[5,6,7,8,9,10,11,12]
lst4=[i+2 for i in lst2]

print(lst4)
