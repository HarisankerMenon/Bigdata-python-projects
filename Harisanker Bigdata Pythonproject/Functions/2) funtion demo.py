'''def fact():
    num=int(input('enter a number'))
    fact=1
    for i in range(1, num + 1):
        fact = fact * i
    print(fact)

fact()

#

def fact(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print(fact)

fact(8)


def fact(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact

res=fact(10)
print(res)
'''
#...................................................

# create a funtion to find cube of a number

'''def cube():
    num = int(input("enter the number"))
    cube= num ** 3
    print(cube)
cube()

def cube(num):
    cube = num ** 3
    print(cube)

cube(2)

def cube(num):
    cube = num ** 3
    return cube
        
res=cube(2)
print(res)'''

#........................................

def even():
    num=int(input("enter a num"))
    if num%2==0:
        print("num is even")

even()

def even(num):
    if num%2==0:
        return num
res=even(10)
print(res)
 