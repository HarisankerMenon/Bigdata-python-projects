# employee
# id, ename , disignation , salary

# 1. print ename

# 2. company dic present or not

# 3. company : value add

# 4. update salary

# 5. print all key value pair

# 6. delete designation

employee={"id":101,"ename":'Harisanker',"designation":'bigdata',"salary":1000}

print(employee["ename"])


print("company" in employee)

employee["company"]='luminar'

print(employee)

employee["salary"]=2000

print(employee)

for i in employee:
    print(i,employee[i])

del employee["designation"]

print(employee)
