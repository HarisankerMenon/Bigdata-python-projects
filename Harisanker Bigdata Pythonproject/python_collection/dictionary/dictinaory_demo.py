dic={"roll":100,"name":'sabir',"age":26,"prof":'bigdata',"salary":1000}

print(dic)

# collect perticular value by using its key

print(dic["name"])

print(dic["prof"])



for i in dic:
    print(i,dic[i])

#...................................................

# how to update a value in dictionary

dic1={"roll":100,"name":'sabir',"age":26,"prof":'bigdata',"salary":1000,"mark1":40}

print(dic1)

dic1["mark1"]=50

print(dic1)

dic1["roll"]=200

dic1["prof"]='python'

dic1["salary"]=2000

dic1["salary"]+=2000

print(dic1)

#...............................................

# to delete a key value

del dic1["mark1"]

print(dic1)

#...............................................


# add a new key value

dic1["mark2"]=45

print(dic1)
#................................................

# to cheak a key present

print("total" in dic1)

print("mark2" in dic1)


