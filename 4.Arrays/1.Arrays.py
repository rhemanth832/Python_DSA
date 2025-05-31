# 4.Arrays
print('Enter the number of elements: ')
num = int(input())  # Convert input directly to int

arr = []

print(f'Enter {num} elements: ')
for i in range(num):
    element = input()
    arr.append(element)

print('The elements are:')
for i in range(num):
    print(arr[i], end=' ')


