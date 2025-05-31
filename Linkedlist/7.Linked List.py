#linked list is a collection of nodes
#node is a data structure that holds a value and a pointer to the next node in the linked list
#the last node in the linked list points to None
#linked list operations are insertion, deletion(operation (for insert, delete) : beginning, end, at specific position)
# traversal (operation: going through all the nodes)
class Nodes:
    def __init__(self, data):
        self.data = data
        self.next = None
node1=Nodes(8)
print(node1.data)
print(node1.next)
#Singly Linkedlist
print("Singly Linkedlist: ")
class Nodes:
    def __init__(self, data):
        self.data = None
node1=Nodes(8)
print(node1.data)


