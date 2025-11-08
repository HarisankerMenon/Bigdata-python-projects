tu=(15,20,25,30,35,40,45,50,55,60)

print(tu)
# tuple is immutable
# change value of 35 ==> 100

lst=list(tu)

lst[4]=100
tu=tuple(lst)

print(tu)


