#Implementation Of Graph
#AdjList, Add Edge, Degree Of Node

class Graph:

    def __init__(self, nodes, isDirected=False):
        self.nodes=nodes
        self.isDirected=isDirected
        self.adjList={}

        for node in self.nodes:
            self.adjList[node]=[]

    def addEdge(self, u, v):
        self.adjList[u].append(v)
        if self.isDirected is False:
            self.adjList[v].append(u)

#Degree: Number of vertex connected
    def degree(self, node):
        return len(self.adjList[node])

#Print the Adjacent List
    def printAdjList(self):
        for node in  self.nodes:
            print(node,"-->", self.adjList[node])


nodes=["A", "B", "C", "D", "E"]

graph=Graph(nodes)

allEdges=[("A", "B"), ("A","C"), ("B", "D"), ("C", "D"), ("C", "E"), ("D", "E")]

for u,v in allEdges:
    graph.addEdge(u, v)

graph.printAdjList()

print()

print("Degree Of Node A is:\n",graph.degree("A"))
