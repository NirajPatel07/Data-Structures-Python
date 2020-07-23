#Binary Tree Traversal
#1. Depth First Search
#2. Breadth First Search
#
#Depth First search is futher classified as
#1.1 PreOrder Traversal
#1.2 PostOreder Traversal
#1.3 InOrder Traversal

class stack(object):
    def __init__(self):
        self.items=[]

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def isEmpty(self):
        return len(self.items)==0

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.isEmpty():
            return self.items[-1].value
    

class Queue(object):
    def __init__(self):
        self.items=[]

    def enqueue(self, value):
        self.items.insert(0, value)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()

    def isEmpty(self):
        return len(self.items)==0

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.isEmpty():
            return self.items[-1].value
            
    


class Node(object):
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,root):
        self.root=Node(root)


    def preorder(self, start, traversal):
        """ root->left->right """
        if start!=None:
            traversal += (str(start.value)+"-")
            traversal=self.preorder(start.left, traversal)
            traversal=self.preorder(start.right, traversal)
        return traversal

    def inOrder(self, start, traversal):
        """left->root->right"""
        if start!=None:
            traversal=self.inOrder(start.left, traversal)
            traversal += (str(start.value)+"-")
            traversal=self.inOrder(start.right, traversal)
        return traversal

    def postorder(self, start, traversal):
        if start!=None:
            traversal=self.postorder(start.left, traversal)
            traversal=self.postorder(start.right, traversal)
            traversal += (str(start.value)+"-")
        return traversal

    def levelOrder(self, start):
        if start is None:
            return

        q = Queue()
        q.enqueue(start)

        traversal=""
        
        while len(q)>0:
            traversal+=str(q.peek()) + "-"
            node = q.dequeue()

            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)

        return traversal
            
        
    def reverseLevelOrder(self, start):
        if start is None:
            return

        q=Queue()
        s=stack()
        q.enqueue(start)

        while len(q)>0:
            node=q.dequeue()
            s.push(node)

            if node.right:
                q.enqueue(node.right)
            if node.left:
                q.enqueue(node.left)

        traversal=""

        while len(s)>0:
            node=s.pop()
            traversal+=str(node.value)+"-"
        return traversal
    
    def height(self, node):
        if node is None:
            return -1
        left_height=self.height(node.left)
        right_height=self.height(node.right)

        return 1+max(left_height, right_height)

    def size(self):
        if self.root is None:
            return 0

        size=1
        s=stack()
        s.push(self.root)
        while s:
            node=s.pop()
            if node.left:
                size+=1
                s.push(node.left)
            if node.right:
                size+=1
                s.push(node.right)
        return size
        
    def printTree(self, traversal_type):
        if traversal_type=="preorder":
            return self.preorder(bt.root, "")

        elif traversal_type=="inorder":
            return self.inOrder(bt.root, "")

        elif traversal_type=="postorder":
            return self.postorder(bt.root, "")

        elif traversal_type=="levelOrder":
            return self.levelOrder(bt.root)

        elif traversal_type=="reverseLevelOrder":
            return self.reverseLevelOrder(bt.root)
        
        else:
            print("Wrong Traversal input")

        
bt=BinaryTree(1)
bt.root.left=Node(6)
bt.root.right=Node(5)
bt.root.left.left=Node(0)
bt.root.left.right=Node(4)
bt.root.right.left=Node(9)
bt.root.right.right=Node(7)
print(bt.printTree("preorder"))
print(bt.printTree("inorder"))
print(bt.printTree("postorder"))
print(bt.printTree("levelOrder"))
print(bt.printTree("reverseLevelOrder"))
print(bt.height(bt.root))
print(bt.size())
