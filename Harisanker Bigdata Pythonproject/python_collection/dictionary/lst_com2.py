# multiple conditon


# syntax

# [print if condition else print range]
lst=[i**3 if i%2==0 else i**2 for i in range(1,51)]

print(lst)

#...........................................................


# 1 to 75
# numer even print square
# number odd print number

lst2=[i**2 if i%2==0 else i for i in range(1,76)]

print(lst2)

#............................................................



# print corresponding i

lst3=[(i,i**2) if i%2==0 else (i,i) for i in range(1,76)]

print(lst3)

#.........................................................



# 1 to 50
# number even print even
# number odd print odd

lst4=[(i,'even') if i%2==0 else (i,'odd') for i in range(1,51)]

print(lst4)

#.....................................................


#  1 to 75

lst5=[i**2 if i%2==0 else 0 if i/5==0 else i for i in range(1,76)]

print(lst5)

lst6=[(i,i**2) if i%2==0 else (i,0) if i/5==0 else (i,i) for i in range(1,76)]

print(lst6)

#.........................................................


# string

# name = sabir

name='sabir'
vowels='aeiouAEIOU'

lst7=['y' if i in vowels else 'n' for i in name]

print(lst7)

#.........................................................


# create lst

lst8=[2,4,6,8,10,12,14,16]



# sqare greater than 100

lst9=[i**2 for i in lst8 if i**2>100]

print(lst9)


