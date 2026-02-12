class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
class BST:
    
    # Insertion
    def insert(self, root, value):
        if root == None:
            return Node(value)
        if root.data == value:
            return root
        if root.data < value:
            root.right = self.insert(root.right, value)
        else:
            root.left = self.insert(root.left, value)
        return root
    
    # deletion
    # def delete(self, value):
    #     if root == None:
    #         print("empty Tree!!")
    #         return
    #     if root.data == value:

    # Searching
    def search(self,root, value):
        if root == None:
            print(f"Element {value} not found!")
            return
        if root.data == value:
            print(f"Element {root.data} found!")
            return
        if root.data > value:
            self.search(root.left, value)
        elif root.data < value:
            self.search(root.right, value)
        return 


    # inOrder Traversal
    def inOrder(self, root):
        if root != None:
            self.inOrder(root.left)
            print(root.data, end=" ")
            self.inOrder(root.right)

    # preOrder Traversal
    def preOrder(self, root):
        if root != None:
            print(root.data, end=" ")
            self.preOrder(root.left)
            self.preOrder(root.right)

    # PostOrder Traversal
    def postOrder(self, root):
        if root != None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data, end=" ")

bst = BST()
root = bst.insert(None, 45)
root = bst.insert(root, 145)
root = bst.insert(root, 15)
root = bst.insert(root, 105)
root = bst.insert(root, 1)
root = bst.insert(root, 71)
root = bst.insert(root, 41)
root = bst.insert(root, 43)

bst.inOrder(root)

bst.search(root, 55)
bst.search(root, 15)
