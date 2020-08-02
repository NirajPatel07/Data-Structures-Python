class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None 

    def insertFirst(self, data):
        new_node = Node(data)
        cur = self.head 
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def insertLast(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def remove(self, value):
        if self.head.data==value:
            curr=self.head
            while curr.next!=self.head:
                curr=curr.next
            curr.next=self.head.next
            self.head=self.head.next
            
        else:
            curr=self.head
            while curr.next!=self.head:
                prev=curr
                curr=curr.next
                if curr.data==value:
                    prev.next=curr.next
                    curr=curr.next

    def __len__(self):
        c=1
        curr=self.head
        while curr.next!=self.head:
            c+=1
            curr=curr.next
        return c

    def splitList(self):
        size=len(self)
        mid=int(size)//2

        if size==0:
            print("List is Empty")
        if size==1:
            print(self.data)

        c=0
        prev=None
        curr=self.head
        while curr and c<mid:
            c+=1
            prev=curr
            curr=curr.next
        prev.next=self.head

        splitList=CircularLinkedList()
        while curr.next!=self.head:
            splitList.insertLast(curr.data)
            curr=curr.next
        splitList.insertLast(curr.data)

        self.view()
        print("\n")
        splitList.view()
        
    def removeNode(self, node):
        if self.head==node:
            curr=self.head
            while curr.next!=self.head:
                curr=curr.next
            curr.next=self.head.next
            self.head=self.head.next
            
        else:
            curr=self.head
            while curr.next!=self.head:
                prev=curr
                curr=curr.next
                if curr==node:
                    prev.next=curr.next
                    curr=curr.next

    def josephus_circle(self, step):
        curr=self.head
        c=1
        while len(self)>1:
            while c!=step:
                c+=1
                curr=curr.next
            print("Removed: ",curr.data)
            self.removeNode(curr)
            curr=curr.next
            
        
            

    def view(self):
        cur = self.head 

        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break


c = CircularLinkedList()
c.insertLast("C")
c.insertLast("D")
c.insertFirst("B")
c.insertFirst("A")
c.view()
print()
c.josephus_circle(2)
c.view()
