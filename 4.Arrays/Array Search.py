# 4.Arrays
print('Enter the number of elements: ')
num = int(input())
arr = []
print(f'Enter {num} elements: ')
for i in range(num):
    element = input()
    arr.append(element)
print('The elements are: ')
for i in range(num):
    print(arr[i], end=' ')
print()
print('Enter the element to be searched: ')
ele = input()
if ele in arr:
    print('The element is present at ',arr.index(ele)+1)
else:
    print('The element is not present in the array')