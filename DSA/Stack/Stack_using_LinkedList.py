class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    

class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0