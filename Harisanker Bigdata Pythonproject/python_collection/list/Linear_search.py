# Linear search


lst=[14,101,15,20,45,60,90,100,150,125,200,250,]

element=int(input("enter a number"))
flg=0

for i in lst:
    if i==element:
        flg=1
        break
    else:
        pass

if(flg>0):
    print("element found")
else:
    print("element not found")

#drawback takes time to do itration



# Binarty search (algoritham)

#:- to reduse time of leniar search

