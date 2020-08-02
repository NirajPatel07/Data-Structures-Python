
# Graph BFS Traversal


# import Queue it will help in bfs traversal
from queue import Queue




class Graph:

    def __init__(self, nodes, isDirected=False):
        self.nodes=nodes
        self.isDirected=isDirected
        self.adjList={}

        for node in nodes:
            self.adjList[node]=[]

    def addEdge(self,u , v):
        self.adjList[u].append(v)
        if self.isDirected  is False:
            self.adjList[v].append(u)


# BFS Traversal
    def bfs(self, root):

        visited={}
        parent={}
        level={}
        op=[]
        queue=Queue()

        for node in self.nodes:
            visited[node]=False
            parent[node]=None
            level[node]=-1

        s=root

        visited[s]=True
        level[s]=0
        queue.put(s)

        while not queue.empty():
            u=queue.get()
            op.append(u)

            for v in self.adjList[u]:
                if visited[v] is False:
                    visited[v]=True
                    parent[v]=u
                    level[v]=level[u]+1
                    queue.put(v)

        return op
        




        

nodes=["A", "B", "C", "D", "E"]

graph=Graph(nodes)

allEdges=[("A", "B"), ("A","C"), ("B", "D"), ("C", "D"), ("C", "E"), ("D", "E")]

for u,v in allEdges:
    graph.addEdge(u, v)


print("BFS Traversal from source node A:\n", graph.bfs("A"))

