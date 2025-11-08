lst=[[101,'arun','k',26,'bigdata',1000],
     [102,'amal','s',27,'python',1500],
     [103,'vishnu','t',24,'python',1200],
     [104,'aslam','k',28,'python',1600],
     [105,'sabir','k',26,'bigdata',2000]]

print(lst)

'''for i in lst:
     print(i)'''

# collect fist name of all employee

'''for i in lst:
     print(i[1])'''

#..................................................

# collect fname lname age prof

'''for i in lst:
     print(i[1],i[2],i[3],i[4])

for i in lst:
     print(i[1:5])'''
#....................................................
# age above and equal to 26

'''for i in lst:
     if i[3]>=26:
          print(i)
'''
#.....................................................

# bigdata fname lname age prof salaer

'''for n in lst:
     if n[4]=="bigdata":
          print(n[1:5])'''


#.....................................................

# python and age above 26 ( fname laname age prof salary)

'''for n in lst:
     if n[4]=="python" and n[3]>=26:
          print(n[1:6])'''


#.....................................................
#  total salary
sum=0
for i in lst:
     sum = sum+i[5]
print(sum)




#.....................................................

# max salary

for i in lst:
     max=max(i[5])
print(max)

