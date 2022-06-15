import dijkstra
import fileHandler
import os
import time

def testDijkstra(files):

    for file in files:

        startTime = time.time()
        print(file.replace("Lab7_files/", ""))
        graph, nodes = fileHandler.fileToGraph(file)
        outputFile = file.replace(".txt", "oD.txt")
        if os.path.exists(outputFile):
            os.remove(outputFile)

        # for source in range(0, nodes):
        source = 0
        dist, parent = dijkstra.dijkstra(graph, source)
        fileHandler.saveSolution(dist, parent, source, outputFile)


        print("Execution time: ", end = " ")
        executionTime = (time.time() - startTime) * 1000
        if executionTime > 1000:
            executionTime = executionTime / 1000
            print("{0:.2f} s".format(executionTime))
        else:
            print("{0:.2f} ms".format(executionTime))

        print("\n")

        
    