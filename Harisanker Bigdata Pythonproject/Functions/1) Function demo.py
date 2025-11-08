# Functions
#.................................

#  :- funtion is used to call a program hence dont whant to reapeat a code and to reduse program length


#    input functions

#       a) print
#       b) input()
#       c) range
#       d) type

#...................................


#   How to create a function


#   1) Function without arguments and no return type
#   2) Function with arguments and no return type
#   3) Function with arguments and return type

# arguments :- variables (in function)


'''def fname(argument):
    fn defenition

call_funtion  (using funtion name)'''

#.......................................


#   1) Function without arguments and no return type

#  eg:-
'''def add():
    num1=int(input("enter number 1"))
    num2=int(input("enter number 2"))
    sum=num1+num2
    print(sum)

add()

add()'''
#..........................................


#   2) Function with arguments and no return type

# eg:-

'''def add(num1,num2):
    sum=num1+num2
    print(sum)

add(20,40)

# arguments:-  num1=20,num2=40

add(30,70)'''

#............................................

#   3) Function with arguments and return type

def add(num1,num2):
    sum=num1+num2
    return sum

res=add(20,40)
print(res)

res1=add(30,70)
print(res1)

