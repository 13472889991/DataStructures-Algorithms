class Node():
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
    def __str__(self):
        return str(self.value)
    def setParent(self, parent):
        self.parent = parent
    def setLeft(self, left):
        self.left = left
    def setRight(self, right):
        self.right = right
    def parent(self):
        return self.parent
    def left(self):
        return self.left
    def right(self):
        return self.right




class BinarySearchTree():
    def __init__(self, value):
        self.root=Node(value)
    
