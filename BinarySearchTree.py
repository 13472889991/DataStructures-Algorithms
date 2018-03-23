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
    def __init__(self, value = None):
        self.root = Node(value)
    def setRoot(self, value):
        self.root = Node(value)
    def insert(self, value):
        if self.root = None
           self.root = Node(value)
        else:
          self.insertNode(self.root, key)
    def insertNode(current, key):
        if key < current.key:
           if current.left:
              self.insertNode(current.left, key)
           else :
              currrent.left_child = Node(key)
        elif key > current.key:
           if current.right:
              self.insertNode(current.right, key)
           else:
              current.right = Node(key)
    # returns the value of the nodes in ascending order
    def __str__(self):
        return self.inOrderTraversal(self,self.root)
    # Given a value of a node, looks through the tree to find node with said value. Returns None if it does not exist
    def find(value, root = None):
        if root == None:
            root=self.root
        while root.value != value and root.value != None:
            if root.value > value :
                root = root.left
            else:
                root = root.right
        return root 
    #Finds the minimum value of a node in the BST
    def min(self, value, root = None ):
        if root == None:
            root = self.root
        while root.left.value != None:
            root = root.left
        return root
    #Finds the maximum value of a node in the BST
    def max(self, value, root = None ):
        if root == None:
            root = self.root
        while root.right.value != None:
            root = root.right
        return root
    #TODO
    def treeSort(self, node = None, nodes = []):
        if node is None:
            node = self.root
        if node.key:
            if node.left:
              self.treeSort(node.left, nodes)
            nodes.append(node.key)
            if node.right:
               self.treeSort(node.right, nodes)
            return nodes
    def preOrderTraversal(self, root = None):
        if root == None:
            root = self.root
        if root.value != None:
            print(root.value)
        if root.left != None:
            self.preOrderTraversal(root.left)
        if root.right!= None:
            self.preOrderTraversal(root.right)
    def inOrderTraversal(self, root = None):
        if root == None:
            root = self.root
        if root.left != None:
            self.preOrderTraversal(root.left)
        if root.value != None:
            print (root.value)
        if root.right != None:
            self.preOrderTraversal(root.right)
    def postOrderTraversal(self, root = None):
        if root == None:
            root = self.root
        if root.left != None:
            self.preOrderTraversal(root.left)
        if root.right != None:
            self.preOderTraversal(root.right)
        if root.value != None:
            print(root.value)
