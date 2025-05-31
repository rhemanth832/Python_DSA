#()-Tuples and they are immutable datatypes
a=(1,2,3,4,5)
print(a)

b=(1,2,3,4,5)
 #b [0]=10 TypeError: 'tuple' object does not support item assignment
#print(b)

c=a+b
print(c)

print("UnPacking")
a,b,c,d,e=(1,2,3,4,5)
print(a)
print(a,e)


