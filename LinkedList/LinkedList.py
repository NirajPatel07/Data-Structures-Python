class node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.start=None;

    def insertFirst(self, value):
        newNode=node(value)
        newNode.next=self.start
        self.start=newNode

    def insertLast(self, value):
        newNode=node(value)
        if self.start==None:
            self.start=newNode
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode

    
                
    def searchList(self, value):
        temp=self.start
        if temp==None:
            print("linked list is empty")
        while temp!=None:
            if temp.data==value:
                print("Enter Value is present in Linkedlist")
                break
            else:
                print("Not present")

    def updateList(self, value1, value2):
        temp=self.start
        while temp!=None:
            if temp.data==value1:
                temp.data=value2
                print("Value Updated")
                break
            else:
                temp=temp.next
            

    def deleteFirst(self):
        if self.start==None:
            print("Linked List is empty")
        else:
            self.start=self.start.next

    def deleteLast(self):
        if self.start==None:
            print("Linked List is empty")
        elif self.start.next==None:
            self.start=None
            Print("There was only 1 element that is deleted")
        else:
            temp=self.start
            while temp.next.next!=None:
                temp=temp.next
            temp.next=None;

    def reverse(self):
        current=self.start
        prev=None
        while current!=None:
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.start=prev

    def length(self):
        temp=self.start
        c=0
        while temp!=None:
            c+=1
            temp=temp.next
        print("Length: ",c)

    def MergeSortedList(self, llist):
        p=self.start
        q=llist.start
        s=None

        if p==None:
            return q
        if q==None:
            return p

        if p!=None and q!=None:
            if p.data<q.data:
                s=p
                p=s.next
            else:
                s=q
                q=s.next
        newHead=s

        while p!=None and q!=None:
            if p.data<q.data:
                s.next=p
                s=p
                p=s.next
            else:
                s.next=q
                s=q
                q=s.next
        if p==None:
            s.next=q
        if q==None:
            s.next=p
        return newHead

    def removeDuplicates(self):
        curr=self.start
        prev=None
        dup_values=[]

        while curr!=None:
            if curr.data in dup_values:
                prev.next=curr.next
                curr=curr.next
            else:
                dup_values.append(curr.data)
                prev=curr
            curr=prev.next

    def nodevalue(self, value):
        curr=self.start
        v=[]
        while curr!=None:
            v.append(curr.data)
            curr=curr.next
        print(v[value-1])

    def countOccurences(self, value):
        curr=self.start
        c=0
        while curr!=None:
            if curr.data==value:
                c+=1
            curr=curr.next
        print(c)
            
    def palindrome(self):
        curr=self.start
        s=""
        while curr!=None:
            s+=curr.data
            curr=curr.next
        print(s)
        if s==s[::-1]:
            print("Palindrome")
        else:
            print("Not a Palindrome")


            
        
    
    def viewList(self):
        if self.start==None:
            print("Linked List is empty")
        else:
            temp=self.start
            while temp!=None:
                print(temp.data,end="-->")
                temp=temp.next

l=LinkedList()
l.insertLast(4)
l.insertLast(5)
l.insertLast(6)
l.viewList()
print("................")
l1=LinkedList()
l1.insertLast(1)
l1.insertLast(2)
l1.insertLast(3)
l1.viewList()

l1.MergeSortedList(l)
l1.viewList()










