# List slicing
#..............


lst=[25,50,75,100,125,150,175,200,225,250,275,300]


print(lst[2])

print(lst[5])

print(lst[2:5])   # 2:- lower limit , 5:- upper limit

print(lst[4:4])


# only lower limit

print(lst[3:])

print(lst[5:])


# only upper limit


print(lst[:0])

print(lst[:3])


# negative index

#-1 to -n

print(lst[-1])
print(lst[-3])
print(lst[-7])

print(lst[-5:-2])   # lst[-5],lst[-4],lst[-3]

print(lst[-7:-3])


print(lst[-4:]) # only lower limit

print(lst[:-5]) # only upper limit


