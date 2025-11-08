# Tuples

#    1) how to define

'''tu=()  # empty tuple
print(type(tu))'''

'''tup=tuple()
print(type(tup))'''


#     2) Hetrogenous Supported or not

'''tu=(10,10,5,'bigdata','python',True)  # sapport hetogenious data

print(tu)'''


#      3) Duplicate value supported or not

tu=(10,10,20,20,30,30,'bigdata','bigdata',True,True,30) # sapport duplicates

print(tu)


#       4)

tu=(10,10,20,20,30,30,'bigdata','bigdata',True,True,30)

print(tu)

#       5) mutable or immutable

tu=(10,15,20,30,35,40,45,50)

tu[2]=50   # immutable

print(tu)



