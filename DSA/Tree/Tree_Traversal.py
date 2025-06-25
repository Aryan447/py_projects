class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)


def printPostorder(root):
    if root:
        printInorder(root.left)
        printInorder(root.right)
        print(root.val)

def printPreorder(root):
    if root:
        print(root.val)
        printInorder(root.left)
        printInorder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Preorder traversal: ")
printPreorder(root)
print("Postorder traversal: ")
printPostorder(root)
print("Inorder traversal: ")
printInorder(root)