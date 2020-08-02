class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None

class doublyLinkedList:
    def __init__(self):
        self.head=None

    def append(self, data):
        if self.head==None:
            newNode=Node(data)
            newNode.prev=None
            self.head=newNode
        else:
            newNode=Node(data)
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=newNode
            newNode.prev=curr
            newNode.next=None

    def prepend(self, data):
        if self.head==None:
            newNode=Node(data)
            newNode.prev=None
            self.head=newNode
        else:
            newNode=Node(data)
            self.head.prev=newNode
            newNode.next=self.head
            self.head=newNode
            newNode.prev=None
            
    def addNodeAfter(self, key, data):
        curr=self.head
        while curr:
            if curr.next==None and curr.data==key:
                self.append(data)
                return
            elif curr.data==key:
                newNode=Node(data)
                nxt=curr.next
                curr.next=newNode
                newNode.next=nxt
                newNode.prev=curr
                nxt.prev=newNode
            curr=curr.next
                    
    def addNodeBefore(self, key, data):
        curr=self.head
        while curr:
            if curr.prev==None and curr.data==key:
                self.prepend(data)
                return
            elif curr.data==key:
                newNode=Node(data)
                prev=curr.prev
                curr.prev=newNode
                prev.next=newNode
                newNode.next=curr
                newNode.prev=prev
            curr=curr.next
        
        

    def delete(self, key):
        curr=self.head
        while curr!=None:
            if curr.data==key and curr==self.head:
                if curr.next==None:
                    curr=None
                    self.head=None
                    return
                else:
                    nxt=curr.next
                    curr.next=None
                    curr=None
                    self.head=nxt
                    nxt.prev=None
                    return
            elif curr.data==key:
                if curr.next!=None:
                    nxt=curr.next
                    prev=curr.prev
                    curr.prev=None
                    curr.next=None
                    curr=None
                    prev.next=nxt
                    nxt.prev=prev
                    return
                else:
                    prev=curr.prev
                    prev.next=None
                    curr.next=None
                    curr.prev=None
                    curr=None
                    return
            curr=curr.next

    def reverse(self):
        temp=None
        curr=self.head
        while curr!=None:
            temp=curr.prev
            curr.prev=curr.next
            curr.next=temp
            curr=curr.prev
        if temp!=None:
            self.head=temp.prev

            
    def removeDuplicates(self):
        curr=self.head
        l=[]
        while curr!=None:
            if curr.data not in l:
                l.append(curr.data)
                curr=curr.next
            else:
                nxt=curr.next
                self.delete(curr.data)
                curr=nxt

    def pairWithSum(self, sumValue):
      
        pair=[]
        p=self.head
        q=None
        while p!=None:
            q=p.next
            while q!=None:
                if p.data+q.data==sumValue:
                    pair.append((p.data,q.data))
                q=q.next
            p=p.next
        print(pair)
    
    def view(self):
        if self.head==None:
            print("List is empty")
        else:
            curr=self.head
            while curr!=None:
                print(curr.data)
                curr=curr.next
            

d=doublyLinkedList()
d.append(1)
d.append(2)
d.append(3)
d.prepend(9)
d.prepend(5)
d.prepend(9)
d.prepend(8)
d.append(1)
d.append(2)
d.append(3)
d.append(1)
d.append(9)
d.append(4)
d.pairWithSum(6)

