# Swapping

'''num1=10
num2=20

print("number1=",num1)
print("number2=",num2)'''

# swapping values of num1 and num2

'''num1=10
num2=20

print("number1=",num1) #10
print("number2=",num2) #20

num1=num2 #num1=20
num2=num1 #num2=20'''

#..........................................................

# 1) using third variable

'''num1=10
num2=20

print("number1=",num1)
print("number2=",num2)

temp=num1 #temp10
num1=num2 #num1=20
num2=temp #temp2=10

print("after swapping") # after swapping (result)

print("number1=",num1)
print("number2=",num2)'''

#..........................................................

# 2) using arthemetic operator

'''num1=10
num2=20

print("number1=",num1)
print("number2=",num2)

print("after swapping using arithemetic operators")

num1=num1+num2  #num1=10+20=30
num2=num1-num2  #30-20 =10
num1=num1-num2  #30-10 =20

print("number1=",num1)
print("number2=",num2)'''

#...........................................................

#  3) single line swapping

num1,num2=10,20

print("before swapping")  # before swapping the numbers
print("number1=",num1)
print("number2=",num2)

num1,num2=num2,num1

print("after swapping")   # after swapping the numbers
print("number1=",num1)
print("number2=",num2)