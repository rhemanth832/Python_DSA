a=[2,3,1,9,10,4,6,1]
big=a[0]

for i in a:
    if i>big:
        big=i
print(big)



a=[11,22,33,34,45,55]
b=a.pop()
print(b)

a=[11,22,33,34,45,55]
b=a.clear()
print(b)

a=[11,22,33,34,45,55]
del a

a=[11,22,33,34,45,55]
b=a.pop(3)
print(b)

a=[11,22,33,34,45,55]
print(a)
a.insert(2,20)
print(a)

a=[10,20,30,40,50,10,20,40,40]
visit=[] # count numbers in 'list'
for i in a:
    if i not in visit:
        print(i,a.count(i),sep=" : ")
        visit.append(i)

a=[10,20,30,10,20,30,50,60,70]
#output [10,20,30], k=2
k=2
v=[]
for i in a:
    if a.count(i)==k:
        if i not in v:
            print(i)
            v.append(i)

a=[10,20,30,10,20,30,50,60,70]
print(sum(a))
print(len(a))
print(min(a))
print(max(a))

a=[10,20,30,10,40,50,50,10,20,40,40]
res=-1
for i in a:
    if a.count(i)>1:
       res = max(i,res)
print(res)

a= 12,3,9,6,21,34,24,5,7,8
# max no of multiples in 3
res=-1
for i in a:
    if i%3==0:
        res = max(i,res)
print(res)




