from collections import deque

stack=deque()

n=int(input())
while n>0:
    rem=n%2
    stack.append(rem)
    n=n//2
bin=""
while len(stack)!=0:
    a=stack.pop()
    bin+=str(a)

print(bin)
