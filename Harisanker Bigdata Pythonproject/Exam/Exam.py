'''for num in range (1,101):
    count = 0
    for i in range(2,(num//2+1)):
        if(num%i==0):
            count = count+1
            break

    if (count==0 and num!=1):
        print("%d"% num, end='  ')'''























'''string=input("enter a string")
j = -1
flag = 0
for i in string:
    if (i!=string[j]):
        flag = 1
        break
    j = j-1
if flag==1:
    print("NOT PALINDROME")
else:
    print("PALINDROME")'''










'''terms = int(input("enter terms"))

n1, n2 = 0, 1
count = 0

if terms <= 0:
   print("Please enter a positive integer")

elif terms == 1:
   print("Fibonacci sequence upto",terms)
   print(n1)

else:
   print("Fibonacci sequence :-")
   while count < terms:
       print(n1)
       nth = n1 + n2

       n1 = n2
       n2 = nth
       count += 1'''


'''n = int(input("Enter the number of rows"))
# outer loop to handle number of rows
for i in range(0, n):
    # inner loop to handle number of columns
    # values is changing according to outer loop
        for j in range(0, i + 1):
            # printing stars
            print("* ", end="")'''


'''num1=1
num2=1
for i in range(6):

    for j in range(1,num2):

        print(num1,end=' ')

        num1+=1

    print()

    num2+=1'''





'''for i in range(1,5):
    for j in range(i+1,6):
        print(j, end = '  ')
    print()
'''

'''numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
count_odd = 0
count_even = 0
for x in numbers:
        if  (x%2!=0):
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)'''


'''n=7

c=0

while(n):

    if(n>5):

        c=c+n-1

        n=n-1

    else:

        break

print(n)

print(c)'''




# 7. none of these. maximum possible length is 79 characters.
# 8.indentation
# 9. single line comment we use #
# 10.b
# 11.a**b
# 12.none of these
# 13.abc
# 14. 0 1 2
# 15.
# 16.no output
# 17.0 1 2 3
# 18.none of these
# 19.lumina
# 20.Hellothere
# 21.42
# 22 D. b a n a n a




for i in range(1,6):
    for j in range(1,6):
        if(j<=i):
            print(i,end=' ')
        else:
            print(j,end=' ')
    print()













