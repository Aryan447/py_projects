class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_debug_visualization(self):
        return {
            "id": id(self),
            "data": self.data,
            "next": id(self.next) if self.next else None
        }

class LinkedList:
    def __init__(self):
        self.head = None

    # Replace the existing get_debug_visualization() method with this one
    def get_debug_visualization(self):
        nodes = []
        edges = []
        current = self.head
        
        while current:
            # Create a simpler node representation
            nodes.append({
                "id": str(id(current)),
                "label": str(current.data),
                "shape": "circle",  # Make nodes circular
                "color": "#00ff00"  # Give nodes a distinct color
            })
            if current.next:
                edges.append({
                    "from": str(id(current)),
                    "to": str(id(current.next)),
                    "arrows": "to",  # Add arrow to show direction
                    "color": "#0000ff"  # Edge color
                })
            current = current.next
        
        return {
            "kind": {"graph": True},
            "nodes": nodes,
            "edges": edges,
            "layout": "dagre",  # Use dagre layout for linear representation
            "options": {
                "hierarchy": {
                    "enabled": True,
                    "direction": "LR"  # Left to right layout
                },
                "physics": False  # Disable physics simulation
            }
        }

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

    def reverseList(self):
        prev = None
        current = self.head
        
        # BREAKPOINT 1: Place breakpoint here to see initial state
        while current:
            # BREAKPOINT 2: Place breakpoint here to see state at start of each iteration
            temp = current.next
            
            # BREAKPOINT 3: Place breakpoint here to see after temp saves the next pointer
            current.next = prev
            
            # BREAKPOINT 4: Place breakpoint here to see after current.next is changed
            prev = current
            
            # BREAKPOINT 5: Place breakpoint here to see after prev is updated
            current = temp
            # BREAKPOINT 6: Place breakpoint here to see after current moves to next node
        
        # BREAKPOINT 7: Place breakpoint here to see final state before head update
        self.head = prev
        # BREAKPOINT 8: Place breakpoint here to see final reversed list

# Test code
if __name__ == "__main__":
    llist = LinkedList()
    # BREAKPOINT 9: Place breakpoint here to see empty list
    llist.insertEnd(1)
    llist.insertEnd(2)
    llist.insertEnd(3)
    # BREAKPOINT 10: Place breakpoint here to see original list
    
    print("Original list:")
    llist.display()
    
    llist.reverseList()
    # BREAKPOINT 11: Place breakpoint here to see final reversed list
    
    print("\nReversed list:")
    llist.display()