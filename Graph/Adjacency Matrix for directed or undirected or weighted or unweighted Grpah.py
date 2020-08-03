def printMatrix(matrix):
    r,c=len(matrix),len(matrix[0])
    for i in range(r):
        for j in range(c):
            print(matrix[i][j], end="\t")
        print()

def unweightedMatrix():
    v,e=map(int,input("Enter no. of vertex and edges:\n").split())
    matrix=[[0]*v for i in range(v)]
    for i in range(e):
        u,v=map(str,input().split())
        u=ord(u)-ord('A')
        v=ord(v)-ord('A')
        matrix[u][v]=1
        matrix[v][u]=1
    return matrix

def weightedMatrix():
    v,e=map(int,input("Enter no. of vertex and edges:\n").split())
    matrix=[[0]*v for i in range(v)]
    for i in range(e):
        u,v,w=map(str,input().split())
        u=ord(u)-ord('A')
        v=ord(v)-ord('A')
        w=int(w)
        matrix[u][v]=w
        matrix[v][u]=w
    return matrix

c=int(input("1. Weighted Matrix\n2.Unweighted Matrix\nEnter Your Choice:\n"))
if c==1:
    op=weightedMatrix()
else:
    op=unweightedMatrix()

printMatrix(op)
