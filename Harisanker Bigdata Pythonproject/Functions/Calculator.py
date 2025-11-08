# using function to ctraeate a calculator


def add():
    num1=int(input("enter num1"))
    num2=int(input("enter num2"))
    sum=num1+num2
    print(sum)


def sub():
    num1 = int(input("enter num1"))
    num2 = int(input("enter num2"))
    sub=num1-num2
    print(sub)

def mul():
    num1 = int(input("enter num1"))
    num2 = int(input("enter num2"))
    mul=num1*num2
    print(mul)


def div():
    num1 = int(input("enter num1"))
    num2 = int(input("enter num2"))
    div=num1/num2
    print(div)


print("select operation")
print("#1 addition")
print("#2 subtraction")
print("#3 multiplication")
print("#4 division")

choise=int(input("enter your choise"))

if(choise==1):
    add()
elif(choise==2):
    sub()
elif(choise==3):
    mul()
else:
    div()


