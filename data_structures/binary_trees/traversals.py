class Node:
    def __init__(self, val):
        self.data = val
        self.leftChild = None
        self.rightChild = None


class Tree:
    def preOrderTraversal(self, rootNode):
        if not rootNode:
            return
        print(rootNode.data)
        self.preOrderTraversal(rootNode.leftChild)
        self.preOrderTraversal(rootNode.rightChild)

    def inOrderTraversal(self, rootNode):
        if not rootNode:
            return
        self.inOrderTraversal(rootNode.leftChild)
        print(rootNode.data)
        self.inOrderTraversal(rootNode.rightChild)

    def postOrderTraversal(self, rootNode):
        if not rootNode:
            return
        self.postOrderTraversal(rootNode.leftChild)
        self.postOrderTraversal(rootNode.rightChild)
        print(rootNode.data)
