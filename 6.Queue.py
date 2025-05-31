#Queue
#Queue in python is a linear data structure.
# It follows FIFO
# at enqueue, append for insertion and at dequeue, pop for deletion
#the first element is removed first
# deque: queue in python are created by the collections module which provides a class called deque
         #Append, and pop are faster in deque than in list
# time complexity: enqueue and dequeue is O(1)
from enum import nonmember

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, data):
        self.queue.append(data)
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    def display(self):
        return self.queue
    def size(self):
        return len(self.queue)
q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print('After enqueuing',q.display())
print('The removed element: ',q.dequeue())
print('After removing element',q.display())
                     #(OR)
lis=list(map(int,input('Enter the elements into the list (by giving spaces): ').split(' ')))
q=Queue()
for i in lis:
    q.enqueue(i)
print('After enqueuing',q.display())
print('The removed element: ',q.dequeue())
print('After removing element',q.display())

