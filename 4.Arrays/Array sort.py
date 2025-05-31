# 4.Arrays
print('Enter the number of elements: ')
num = int(input())
arr = []
print(f'Enter {num} elements: ')
for i in range(num):
    element = input()
    arr.append(element)
print('The elements are:')
for i in range(num):
    print(arr[i], end=' ')
print()
temp=0
for i in range(num):
    for j in range(num-i-1):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print('Sorted array is:')
for i in range(num):
    print(arr[i], end=' ')

