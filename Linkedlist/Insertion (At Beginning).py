#Linked list Insertion at the beginning
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class sll:
    def __init__(self):
        self.head = None
    def traverse(self):
        if self.head is None:
            print("Singly Linkedlist")
        else:
            while self.head is not None:
                print(self.head.data, end=" ")
                self.head = self.head.next
    def insert_at_beg(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
n1=Node(5)
sll1=sll()
sll1.head=n1
n2=Node(10)
n1.next=n2
n3=Node(15)
n2.next=n3
n4=Node(20)
n3.next=n4
sll1.insert_at_beg(2)
sll1.traverse()
