adjList={ "A":["C", "B"], "B":["D"], "C":[], "D":["A", "E"], "E":[] }

color={}
parent={}

for node in adjList.keys():
    color[node]="W"
    parent[node]=None

def dfs(u):
    color[u]="G"

    for v in adjList[u]:
        if color[v]=="W":
            parent[v]=u
            dfs(v)
        elif color[v]=="G" and parent[u]!=v:
            print("Cycle Found: ", u, "to", v)

    color[u]="B"

for u in adjList.keys():
    if color[u]=="W":
        dfs(u)
