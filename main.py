import test
import fileHandler

if __name__ == '__main__':

    graphFiles = ['g7.txt', 'g9.txt']
    graphFiles = list(map(lambda filename: "Lab7_files/" + filename, graphFiles))

    for i in range(1, 4):

        customGraph, edges = fileHandler.my_graph_generator(10 ** i, 0.4)
        graphFile = f"Lab7_files/g{10 ** i}.txt"
        fileHandler.graphToFile(customGraph, edges, graphFile)
        graphFiles.append(graphFile)
        # print(customGraph)
        

    test.testDijkstra(graphFiles)