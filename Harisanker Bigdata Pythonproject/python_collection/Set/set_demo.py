# set

#     1)  how to define

'''st={}

print(type(st))'''

'''set={1,2,3,4,5}

print(type(set))'''


st=set()           # to create empty set

print(type(st))


#     2) support hetrogenious data or not


st1={10,10,5,'bigdata','python',True}   # supports hetogenious data

print(st1)


#      3) support duplicate or not

st2={10,10,15,15,'bigdata','bigdata'}

print(st2)

#      4)

st3={1,0,3,True,False}   #true=1,false=0 ( hence do not take duplicates)

print(st3)

st4={2,5,3,True,False}         

print(st4)


#       5) insertion order is preseved or not


st5={2,5,3,True,False}             # insertion order is not preserved

print(st5)


#         6) mutable or immutable

#              set is mutable
