import sys

def dijkstra(graph, src):
 
    row = len(graph)
    dist = [sys.maxsize] * row
    parent = [-1] * row
    dist[src] = 0
    queue = [i for i in range(row)]
             
    while queue:

        u = minDistance(dist,queue)

        if u == -1:
            return (dist, parent)

        queue.remove(u)

        for i in range(len(graph[0])):
            if graph[u][i] and i in queue:
                if dist[u] + graph[u][i] < dist[i]:
                    dist[i] = dist[u] + graph[u][i]
                    parent[i] = u
        
            
    return (dist, parent)


def minDistance(dist, queue):
        
    minimum = sys.maxsize
    min_index = -1
         
    for i in range(len(dist)):
        if i in queue and dist[i] < minimum:
            minimum = dist[i]
            min_index = i

    return min_index
