# Dictionary

#  key-value pairs :- value assigined

# roll : 101
# name : sabir

# key==roll
# value==name


#     1) how to define

'''dic={}'''

print(type(dic))

dic1={"roll":101,"name":'sabir',"age":26,"prof":'bigdata',"salarary":1000}

print(dic1)
#.......................................................


# merge sort
# binary sort



#      2) hetrogenious data support or not

dic2={"roll":101,"name":'sabir',"age":26,"prof":'bigdata',"salarary":1000}

print(dic2)   # hetrogenious data supported


#......................................................

#       3) duplicates supported or not


dic3={"roll":101,"name":'sabir',"age":26,"prof":'bigdata',"salarary":1000,"roll":102}

print(dic3) # duplicate not supported



dic4={"roll":101,"name":'sabir',"age":26,"prof":'bigdata',"salarary":1000,"mark1":102}

print(dic4)  # duplicate value supported not key

#..........................................................


#        4) insertion order preserved or not


dic5 = {"roll": 101, "name": 'sabir', "age": 26, "prof": 'bigdata', "salarary": 1000, "mark1": 102}

print(dic5)     # insertion order preserved

#..........................................................


#        5) mutable or immutable

# dictionary is mutable