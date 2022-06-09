from random import randint, random
import numpy as np

def fileToGraph(filename):

    with open(filename, 'r') as f:

        lines = f.readlines()
        lines = [line.rstrip() for line in lines]

        data = [line.split() for line in lines]

        nodes = int(data[0][0])
        graph = [[0 for j in range(nodes)]for i in range(nodes)]

        for item in data[1:]:
            i = int(item[0])
            j = int(item[1])
            graph[i][j] = int(item[2])
            # below line if graph is one-directional (1 -> 0 = 0 -> 1)
            graph[j][i] = int(item[2])
                
        return (graph, nodes)


def graphToFile(graph, edges, filename):

    with open(filename, 'w') as f:

        nodes = len(graph)
        f.write(str(nodes) + " ")
        f.write(str(edges) + "\n")
        for i in range(len(graph)):
            for j in range(len(graph[0])):
                f.write(str(i) + " " + str(j) + " " + str(graph[i][j]) + "\n")

def saveSolution(dist, parent, src, file):

    with open(file, 'a') as f:

        for i in range(len(dist)):
            if i == src:
                continue
            path = []
            savePath(path, parent, i)
            edges = len(path) - 1
            newPathString = ','.join([str(num) for num in path])
            writeToFile = f"{src} {i} {dist[i]} {edges} {newPathString}\n"
            f.write(writeToFile)



def savePath(path, parent, j):
         
    if parent[j] == -1:
        path.append(j)
        return
    savePath(path, parent , parent[j])
    path.append(j)



def my_graph_generator(n, p):

    v = 0
    graph = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if random() < p:
                if graph[i][j] == 0:
                    random_weight = randint(1, 10)
                    graph[i][j] = random_weight
                    graph[j][i] = random_weight
                    v += 1

    return graph, v
# def generate_random_graph(n, p, directed = False):

#     nodes = range(n)
#     no_edges = 0
#     adj_list = [[0 for j in nodes]for i in nodes]
#     possible_edges = product(nodes, repeat = 2) if directed else combinations(nodes, 2)
#     for u, v in possible_edges:
#         if random() < p:
#             random_index = randint(0, n - 1)
#             random_weight = randint(1, 10)
#             adj_list[u][random_index] = random_weight
#             no_edges += 1
#             if not directed:
#                 adj_list[random_index][u] = random_weight

#     return (adj_list, no_edges)


# def generate_random_graph_v2(n, p, directed = False):

#     nodes = range(n)
#     no_edges = 0
#     adj_list = [[0 for j in nodes]for i in nodes]
#     for u in nodes:
#         if random() < p:
#             random_index = randint(0, n - 1)
#             random_weight = randint(1, 10)
#             adj_list[u][random_index] = random_weight
#             no_edges += 1
#             if not directed:
#                 if adj_list[random_index][u] != 0:
#                      adj_list[random_index][u] = random_weight

#     return (adj_list, no_edges)


# def generate_graph(n, range_from = 0, range_to = 7):

#     v = 0
#     graph = list(range(n))
#     rd = np.random.randint(0, 2, (n, n))
#     for i in range(n):
#         edges = []
#         for j in range(n):
#             if rd[i][j] == 1 and i != j:
#                 edges += [j, randint(range_from, range_to)]
#                 v = v + 1

#         graph[i] = edges

#     return v, graph