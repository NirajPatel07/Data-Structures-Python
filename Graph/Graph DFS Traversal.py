adjList={"A":["B","C"], "B":["D", "E"], "C":["B", "F"], "D":[], "E":["F"], "F":[] }


color={}
parent={}
travTime={}
op=[]

for node in adjList.keys():
    color[node]="W"
    parent[node]=None
    travTime[node]=[-1, -1]

time=0

def dfsUtil(u):
    global time
    color[u]="G"
    travTime[u][0]=time
    op.append(u)
    time+=1

    for v in adjList[u]:
        if color[v]=="W":
            parent[v]=u
            dfsUtil(v)
       
    color[u]="B"
    travTime[u][1]=time
    time+=1

for u in adjList.keys():
    if color[u]=="W":
        dfsUtil(u)

print(op)
print(color)
print(travTime)

