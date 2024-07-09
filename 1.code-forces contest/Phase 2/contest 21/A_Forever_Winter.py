from collections import defaultdict




t = int(input())

def main(graph):

    vertices, edges= list(map(int, input().split()))
    def createGraph(graph,edges):
        for _ in range(edges):
            i, j =list(map(int, input().split()))
            graph[i].append(j)
            graph[j].append(i)

        return graph
    
    graph=createGraph(graph, edges)
    theCount=tuple(graph.values())
    findParent=set()

    for val in theCount:
        if len(val)==1:
            findParent.add(val[0])

    x=len(findParent)
    y= len(graph[list(findParent)[0]])-1

    print(x,y)

for _ in range(t):
    graph= defaultdict(list)
    main(graph)



