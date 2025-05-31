#Stack
#Stack in python is a linear data structure.
# It follows LIFO
# append for insertion and pop for deletion
#last element is removed first
# deque: stack in python are created by the collections module which provides a class called deque
         #Append and pop are faster in deque than in list
stack=[]
stack.append('Welcome')
stack.append('to')
stack.append('Geeks')
stack.append('for')
stack.append('Geeks')
print(stack)
print(stack.pop())
print(stack)
stack.pop()
print(stack)
print()
print('Importing deque from collections')
#importing deque
from collections import deque
stack=deque()
stack.append('Welcome')
stack.append('to')
stack.append('Geeks')
stack.append('for')
stack.append('Geeks')
print(stack)
print(stack.pop())
print(stack)
stack.pop()
print(stack)

#stack implementing using queue
#in stack using queue put to insert and get to delete elements
print('Stack using queue')
from queue import LifoQueue
stack=LifoQueue(maxsize=5) # max size to allocate max elements into queue
stack.put('Welcome')
stack.put('to')
stack.put('Geeks')
stack.put('for') #put insert elements
stack.put('Geeks')
print(stack.qsize()) #returns the number of elements in queue
print(stack.full()) #returns true if queue is full
print(stack.get()) #removes and returns an item from the queue
print(stack.qsize())
print(stack.full())



