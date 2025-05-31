class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class sll:
    def __init__(self):
        self.head = None

    def traversal(self):
        if self.head is None:
            print('singly linkedlist')
        else:
            a = self.head
            while a is not None:
                print(a.data, end='')
                if a.next is None:
                    print('->NULL', end='')
                else:
                    print('->', end='')

                a = a.next

    def min(self):
        a = self.head
        min = self.head.data
        while a is not None:
            if a.data < min:
                min = a.data
            a = a.next
        print('\nMinimum element is: ', min)

    def at_end(self, data):
        a = Node(data)
        curr = self.head
        if self.head is None:
            self.head = a
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = a

    def sum_elements(self):
        sum = 0
        a = self.head
        while a is not None:
            sum = sum + a.data
            a = a.next
        print('\nsum is: ', sum)

    def max(self):
        max = self.head.data
        a = self.head
        while a is not None:
            if a.data > max:
                max = a.data
            a = a.next
        print('\nMaximum Element is :', max)

    def search(self):
        a = self.head
        ele = int(input('Enter the Element to be searched: '))
        flag = 0
        pos = 1
        while a is not None:
            if ele == a.data:
                flag = 1
                print('found at ', pos)
            a = a.next
            pos = pos + 1
        if flag == 0:
            print('Not Found')


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class sll:
    def __init__(self):
        self.head = None

    def traversal(self):
        if self.head is None:
            print('singly linkedlist')
        else:
            a = self.head
            while a is not None:
                print(a.data, end='')
                if a.next is None:
                    print('->NULL', end='')
                else:
                    print('->', end='')

                a = a.next

    def min(self):
        a = self.head
        min = self.head.data
        while a is not None:
            if a.data < min:
                min = a.data
            a = a.next
        print('\nMinimum element is: ', min)

    def at_end(self, data):
        a = Node(data)
        curr = self.head
        if self.head is None:
            self.head = a
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = a

    def sum_elements(self):
        sum = 0
        a = self.head
        while a is not None:
            sum = sum + a.data
            a = a.next
        print('\nsum is: ', sum)

    def max(self):
        max = self.head.data
        a = self.head
        while a is not None:
            if a.data > max:
                max = a.data
            a = a.next
        print('\nMaximum Element is :', max)

    def search(self):
        a = self.head
        ele = int(input('Enter the Element to be searched: '))
        flag = 0
        pos = 1
        while a is not None:
            if ele == a.data:
                flag = 1
                print('found at ', pos)
            a = a.next
            pos = pos + 1
        if flag == 0:
            print('Not Found')


sll1 = sll()
n = int(input('Enter no of Nodes: '))
print('enter the node data: ')
for i in range(n):
    sll1.at_end(int(input()))
sll1.traversal()
sll1.sum_elements()
sll1.max()
sll1.min()
sll1.search()
sll1.del_fir()
sll1.traversal()
sll1.del_end()
sll1.traversal()

sll1 = sll()
n = int(input('Enter no of Nodes: '))
print('enter the node data: ')
for i in range(n):
    sll1.at_end(int(input()))
sll1.traversal()
sll1.sum_elements()
sll1.max()
sll1.min()
sll1.search()
sll1.del_fir()
sll1.traversal()
sll1.del_end()
sll1.traversal()
