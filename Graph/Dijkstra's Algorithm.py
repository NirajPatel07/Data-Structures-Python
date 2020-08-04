import heapq
from collections import defaultdict

def dijkstras(graph, src, dest):
    h=[]
    heapq.heappush(h,(0,src))
    

    while len(h)!=0:
        currcost, currvtx=heapq.heappop(h)
        if currvtx == dest:
            print("Path Exists {} to {} with cost {}".format(src, dest, currcost))
            break
        for neigh, neighcost in graph[currvtx]:
            heapq.heappush(h,(currcost+neighcost,neigh))
            



graph=defaultdict(list)
v,e=map(int, input().split())
for i in range(e):
    u,v,w=map(str,input().split())
    graph[u].append((v, int(w)))

src,dest=map(str, input().split())
dijkstras(graph,src,dest)
