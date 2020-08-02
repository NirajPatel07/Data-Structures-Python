class Stack():
    def __init__(self):
        self.items=[]

    def push(self, item):
        self.items.append(item)

    def pop(self):
            return self.items.pop()

    def viewStack(self):
        if self.items==[]:
            print("Stack is Empty")
        else:
            print(self.items)

    def peek(self):
        if self.items==[]:
            print("Stack is Empty")
        else:
            print(self.items[-1])

    def length(self):
        print(len(self.items))

    def isEmpty(self):
        return self.items==[]

    

    #Stack Application

    def is_match(self, p1, p2):
        if p1 == "(" and p2 == ")":
            return True
        elif p1 == "{" and p2 == "}":
            return True
        elif p1 == "[" and p2 == "]":
            return True
        else:
            return False


    def is_paren_balanced(self, paren_string):
        
        is_balanced = True
        index = 0

        while index < len(paren_string) and is_balanced:
            paren = paren_string[index]
            if paren in "([{":
                s.push(paren)
            else:
                if self.isEmpty():
                    is_balanced = False
                else:
                    top = self.pop()
                    if not self.is_match(top, paren):
                        is_balanced = False
            index += 1

        if self.isEmpty() and is_balanced:
            return True
        else:
            return False


    def intToBin(self, decNum):
        while decNum>0:
            rem=decNum%2
            self.push(rem)
            decNum= decNum//2

        s=""
        while self.items!=[]:
            s+=str(self.pop())
        print(s)
            
            


s=Stack()
s.intToBin(95)
