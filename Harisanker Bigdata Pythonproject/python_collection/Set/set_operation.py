# set operations

#          1) Union
#          2) Intersection
#          3) Diffrence



#    1) Union

# to compain two set

# do not sapport duplicate

st1={1,2,3,4,5,6,7,7,8,9,10}

st2={6,7,8,9,10,11,12,13,14,15}

st3=st1.union(st2)

print(st3)


#    2)Intersection

# collect common elements

st4=st1.intersection(st2)

print(st4)

#     3) Difference

#

st5=st1.difference(st2)

print(st5)

st6=st2.difference(st1)

print(st6)