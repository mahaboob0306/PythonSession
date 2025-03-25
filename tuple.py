#Ordered collections immutable and hetrogeneous datatype
tup=(1,2,3,4,5,7,"hekllo",4,6,3,3,3,True)
print(tup)
print(tup.count(3))
print(tup.index(3))
tup1=5,7,8
tup2=9,2,9
tup3=tup1+tup2
print(tup3)
tupe=(1,2,4)*10
print(tupe)
tupee=(1,2,3,4,5)
print(tupee[1:4])
print(tupee[:4])
print(tupe[-3:])
tup=("apple","Mango","Banana")
print(tup)
a,b,c=tup
print(a)
print(b)
print(c)
print(len(tup))
print("Apple" not in tup)

#for loop
for item in tup:
    print(item)

tup=(5,8,9,3,1)
tp=tuple(sorted(tup))

print(tp)
print(max(tup))
print(min(tup))
print(sum(tup))
lst=[1,3,5,2,7,8,4,6]
#Print lst to tuple
print(lst)
print(tuple(lst))
#print tuple to list
my_tup=(9,46,2,"hello",9,3)
print(my_tup)
print(list(my_tup))
