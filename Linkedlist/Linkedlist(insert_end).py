class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class sll:
    def __init__(self):
        self.head = None

    def traversal(self):
        a = self.head
        if a is None:
            print('Singly Linkedlist')
        else:
            while a is not None:
                print(a.data, end='')
                if a.next is not None:
                    print('->', end='')
                else:
                    print('->NULL')
                a = a.next

    def at_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def at_end(self, data):
        new_node = Node(data)
        curr = self.head
        while curr.next is not None:
            curr = curr.next

        curr.next = new_node


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




