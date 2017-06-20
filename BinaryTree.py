class BinaryTree:

    def __init__(self, rootObj):
        self.root = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            temp = self.leftChild
            self.leftChild = BinaryTree(newNode)
            newNode.leftChild = temp

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            temp = self.rightChild
            self.rightChild = BinaryTree(newNode)
            newNode.rightChild = temp

    def getRoot(self):
        return self.root

    def getLeftVal(self):
        return self.leftChild

    def getRightval(self):
        return self.rightChild

one = BinaryTree(1)
one.insertLeft(2)
one.insertRight(3)
