'''dic={"sedan":1500,'suv':2000,"picup":2500,"minivan":1600,"van":2400,"semi":13600}

# collet key of value > 3000

lst=[i.upper() for i in dic if dic[i]>3000]

print(lst)
'''

# 1) create lst [1 to 100]

#      a) find all of the number that are divisible by 8
#      b) find all of the numbers form (1 to 1000) that have 6 in them
#      c) count number of spaces in a string
#      d) remove all vowels in the string
#      e) find all of the word in a string that are less than 5 letters


lst=[i for i in range(1,1001)]

print(lst)

#   a)

lst1=[i for i in range(1,1001) if i%8==0]

print(lst1)

#   b)

lst2=[i for i in lst if '6'in str(i)]

print(lst2)


#   c)

str="Practice Problems to Drill list comprehension in your head"

lst4=len([i for i in str if i==" "])

print(lst4)


#   d)

vowels="aeiouAEIOU"

lst5=[i for i in str if i not in vowels]

print(lst5)


#    e)

words=str.split(" ")

lst6=[i for i in words if len(i)<5]

print(lst6)



