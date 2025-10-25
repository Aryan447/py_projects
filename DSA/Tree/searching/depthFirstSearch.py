class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def dfs(root):
    if root:
        dfs(root.left)
        print(root.data, end=" ")
        dfs(root.right)


root = Node(5)
root.left = Node(4)
root.right = Node(8)

root.left.left = Node(1)
root.left.right = Node(2)

root.right.left = Node(6)
root.right.right = Node(7)

dfs(root)
print("\n")
