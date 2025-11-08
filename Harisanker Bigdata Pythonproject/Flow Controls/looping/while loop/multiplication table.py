# multipliation table :-

#number:- 6

# 1*6=6
# 2*6+12
#........


# number = int(input ("Enter the number of which the user wants to print the multiplication table: "))
# count = 1
# # we are using while loop for iterating the multiplication 10 times
# print ("The Multiplication Table of: ", number)
# while count <= 10:
#     number = number * 1
#     print (number, 'x', i, '=', number * count)
#     count += 1
#


'''number = int(input("enter number for multiplication table"))
i=1
while(i<=10):
    res=i*number
    print(i,"*",number,"=",res)
    i+=1

number = int(input("enter number for multiplication table"))
i=1
while(i<=10):

    print(i,"*",number,"=",i*number)
    i+=1'''


#...........................................................................

# Limit

'''limit=int(input("enter limit number"))

i=1
while(i<=limit):
    print(i)
    i+=1'''

#............................................................................

# lowe limt and upper limit

'''l_limit=int(input("enter lower limit"))
up_limit=int(input("enter upper limit"))

i=l_limit
while(i<=up_limit):
    print(i)
    i+=1


#or

l_limit=int(input("enter lower limit"))
up_limit=int(input("enter upper limit"))

while(l_limit<=up_limit):
    print(l_limit)
    l_limit+=1'''

#...........................................................

# even numbers

'''l_limit=int(input("enter lower limit"))
up_limit=int(input("enter upper limit"))

while(l_limit<=up_limit):
    print(l_limit)
    l_limit+=2



# or


l_limit=int(input("enter lower limit"))
up_limit=int(input("enter upper limit"))

while(l_limit<=up_limit):
    if(l_limit%2==0):
        print(l_limit)
    l_limit+=1'''

#..............................................................

# odd numbers

l_limit=int(input("enter lower limit"))
up_limit=int(input("enter upper limit"))

while(l_limit<=up_limit):
    if(l_limit%2!=0):
        print(l_limit)
    l_limit+=1

#or

l_limit=int(input("enter lower limit"))
up_limit=int(input("enter upper limit"))

while(l_limit<=up_limit):
    if(l_limit%2==1):
        print(l_limit)
    l_limit+=1