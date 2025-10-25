class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def insertBegin(self, data):
        new_Node = Node(data)
        if self.head is None:
            self.head = new_Node
            return
        else:
            new_Node.next = self.head
            self.head = new_Node

    def insertEnd(self, data):
        new_Node = Node(data)
        if self.head is None:
            self.head = new_Node
            return
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_Node




list1 = LinkedList()

list1.head = Node("Mon")

d2 = Node("Tue")
d3 = Node("Wed")

list1.head.next = d2
d2.next = d3

list1.insertBegin("Sun")
list1.insertEnd("Thu")

list1.display()
