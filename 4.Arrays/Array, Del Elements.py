#Deleting Elements in Array
print('Enter the number of elements: ')
num = int(input())
arr=[]
print('Enter ' + str(num) + ' elements: ')
for i in range(num):
    arr.append(input())
print('Enter the element to be deleted: ')
ele=input()
if ele in arr:
    arr.remove(ele)
    print('The new array is: ')
    for i in range(num-1):
        print(end=arr[i]+' ')
else:
    print('The element is not present in the array')
