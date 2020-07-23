class Node:
    def __init__(self, data=None):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def insert(self, data):
        if self.root is None:
            self.root=Node(data)

        else:
            self._insert(data, self.root)

    def _insert(self, data, currNode):
        if data<currNode.data:
            if currNode.left is None:
                currNode.left=Node(data)
            else:
                self._insert(data, currNode.left)

        elif data>currNode.data:
            if currNode.right is None:
                currNode.right=Node(data)
            else:
                self._insert(data, currNode.right)

        else:
            print("Value is already present in tree")

    def find(self, data):
        if self.root:
            isFound= self._find(data, self.root)
            if isFound:
                return True
            else:
                return False
        else:
            return None

    def _find(self, data, currNode):
        if data>currNode.data and currNode.right:
            return self._find(data, currNode.right)
        elif data<currNode.data and currNode.left:
            return self._find(data, currNode.left)
        if data==currNode.data:
            return True

    def isBstSatisfied(self):
        if self.root:
            is_satisfied=self._isBstSatisfied(self.root, self.root.data)

            if is_satisfied is None:
                return True
            return False
        return True

    def inOrderPrint(self):
        if self.root:
            self._inOrderPrint(self.root)

    def _inOrderPrint(self, curr):
        if curr:
            #if curr.left:
            self._inOrderPrint(curr.left)
            print(str(curr.data))
            #if curr.right:  
            self._inOrderPrint(curr.right)

    def _isBstSatisfied(self, curr, data):
        if curr.left:
            if data>curr.left.data:
                return self._isBstSatisfied(curr.left, curr.left.data)
            else:
                return False

        if curr.right:
            if data<curr.right.data:
                return self._isBstSatisfied(curr.right, curr.right.data)
            else:
                return False

            
                

bst=BST()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)
print(bst.find(4))
print(bst.isBstSatisfied())
bst.inOrderPrint()
