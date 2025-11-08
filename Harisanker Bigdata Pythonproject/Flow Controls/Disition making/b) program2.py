'''num=int(input('enter you number'))

if(num>5):
    print('number is greater than 5')
elif(num==0):
    print('non posative or negative')
elif(num>0):
    print("number is posative")
else:
    print('number is negative')'''

#......................................................

'''num1=int(input('enter number1'))
num2=int(input('enter number2'))

if(num1>num2):
    print('number1 is largest',num1)
elif(num1==num2):
    print("number1 and number2 are equal")
else:
    print("number2 is largest")'''


#......................................................

'''num1=int(input('enter number1'))
num2=int(input('enter number2'))
num3=int(input('enter number3'))

if(num1>num2):
    print('number1 is largest')
elif(num2>num3):
    print("number2 is largest")
elif(num2<num3):
    print('number3 is largest')
else:
    print("number2 is largest")'''

#.......................................................

'''sub1=int(input("enter mark1"))
sub2=int(input("enter mark2"))
sub3=int(input("enter mark3"))
sub4=int(input("enter mark4"))

total=(sub1+sub2+sub3+sub4)
print(total)



if(total>=180):
    print("A+")
elif(total>=160)&(total<=179):
    print("A")
elif(total>=140)&(total<=159):
    print("B+")
elif(total>=120)&(total<=139):
    print("B")
elif(total>=100)&(total<=119):
    print("C+")
elif(total>=80)&(total<=99):
    print("c")
elif(total>=60)&(total<=79):
    print("D+")
else:
    print("fail")'''


#......................................................


'''cost=int(input("enter cost"))


if(cost>100000):
    tax=(15/100)*cost
elif(50000>cost<=100000):
    tax=(10/100)*cost
else:
    tax=(5/100)*cost

print("tax is",tax)'''


#..........................................................


'''city=str(input("enter city"))

if(city=="delhi"):
    print("monument:- Red_fort")
elif(city=="agra"):
    print("monument is Taj_mahal")
elif(city=="jaipur"):
    print("monument is Jal_mahal")

else:
    print("invalied city")'''

#.............................................................

# nested if

'''num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))

if(num1>num2)&(num1>num3):
    if(num2>num3):
        print("numner2 is second lreatest",num2)
    else:
        print("number3 is second largest",num3)
elif(num2>num1)&(num2>num3):
    if(num1>num3):
        print("number1 is second largest",num1)
    else:
        print("number 3 is second largest",num3)
elif(num3>num1)&(num3>num2):
    if(num1>num2):
        print("number1 is second largest",num1)
    else:
        print("number2 is second largest",num2)

'''

#......................................................

cur_year = int(input("Enter current year"))
cur_month = int(input("Enter current month"))
cur_date = int(input("Enter current date"))
bir_year = int(input("Enter your birth year"))
bir_month = int(input("Enter your birth month"))
bir_date = int(input("Enter your birth  date"))
if cur_month == bir_month:
    if cur_date >= bir_date:
         age = cur_year - bir_year
         print("Your age is ", age)
    else:
        age = (cur_year - bir_year) - 1
        print("Your age is ", age)

elif cur_month < bir_month:
    age = (cur_year - bir_year) - 1
    print("Your age is",age)

else:
    age = cur_year - bir_year
    print("Your age is ", age)





#or

'''import datetime

print("##### Welcome to age calculator ######")
birth_year = int(input("Enter your year of birth: \n"))
birth_month = int(input("Enter your month of birth: \n"))
birth_day = int(input("Enter your day of birth: \n"))

current_year = datetime.date.today().year
current_month = datetime.date.today().month
current_day = datetime.date.today().day

age_year = current_year - birth_year
age_month = abs(current_month - birth_month)
age_day = abs(current_day - birth_day)

print("Your exact age is: ", age_year, "Years", age_month, "months and", age_day, "days")'''