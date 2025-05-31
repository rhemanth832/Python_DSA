class Node:
    def __init__(self, data):  # node contains data & next ptr
        self.data = data
        self.next = None


class sll:
    def __init__(self):  # sll references head for total
        self.head = None

    def traversal(self):
        a = self.head  # head should not go end, so it is assigned to a variable
        if a is None:  # if we give not elements to a linkedlist inorder to know singly linkedlist we use it]

            print('Singly Linkedlist is empty')
        else:
            while a is not None:
                print(a.data, end='')
                if a.next is not None:
                    print('->', end='')
                else:
                    print('->NULL')
                a = a.next

    def at_begining(self, data):
        new_node = Node(data)  # creation of new node
        new_node.next = self.head  # linking of new node next to head
        self.head = new_node  # updation of head to new node

    def at_end(self, data):
        new_node = Node(data)  # creation of new node
        curr = self.head  # using of curr node as head temperorily for not head updating to end
        while curr.next is not None:  # until before the last node
            curr = curr.next  # traversing each node

        curr.next = new_node  # link last node to new node

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count = count + 1
            current = current.next
        print(count)

    def at_middle(self, data):
        prev = None
        curr = self.head
        temp = Node(data)
        pos = int(input('Enter the position: '))
        c = 0
        while c < pos - 1:
            prev = curr
            curr = curr.next
            c = c + 1
        prev.next = temp
        temp.next = curr


a1 = Node(5)
sll1 = sll()
sll1.head = a1
a2 = Node(10)
a1.next = a2
a3 = Node(15)
a2.next = a3

sll1.at_begining(2)
sll1.at_end(20)
sll1.traversal()
sll1.size()
sll1.at_middle(7)
sll1.size()

sll1.traversal()

