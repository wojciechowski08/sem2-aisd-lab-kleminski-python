
import operator
import sys


class Graph:

    def __init__(self):
        """
        Creates graph data structure. Built out of verticles, and edges.
        Every vertex has its own unique name which can be string, integer or float.
        """
        self.graph = {}

        self.status = {}
        """
        0 - no knowledge
        1 - knows truth
        -1 - knows fake
        
        status = { "vertexName" : [status, timeInCurrentStatus] , ... }
        
        """



    def addVertex(self, vertex):

        if not vertex in self.graph:
            self.graph[vertex] = []
            self.status[vertex] = []
            self.status[vertex].append(0)  # status
            self.status[vertex].append(0)  # how long in current status
            # print("Vertex " + str(vertex) + " added to graph.")
        else:
            print(str(vertex) + " already in graph, try different name.")


    def addEdge(self, vert1, vert2):

        if vert1 in self.graph and vert2 in self.graph:
            (self.graph[vert1]).append(vert2)
            (self.graph[vert2]).append(vert1)

            # print("Edge between " + str(vert1) + " and " + str(vert2) + " added succesfully.")
        else:
            print("Could not add edge, missing vertex.")


    def viewVerticles(self):
        if len(self.graph) != 0:
            verts = ""
            for i in self.graph:
                verts += str(i) + " "
            print(verts)
        else:
            print("No verticles.")


    def viewEdges(self):
        if len(self.graph) != 0:
            edges = ""
            for i in self.graph:
                if len(self.graph[i]) != 0:
                    for j in self.graph[i]:
                            edges += str(i) + " --- " + str(j) + "\n"
            if edges == "":
                print("No edges between verticles.")
            else:
                print(edges)
        else:
            print("No verticles, so no edges.")


    def size(self):
        m = 0
        if len(self.graph) != 0:
            for i in self.graph:
                if len(self.graph[i]) != 0:
                    for j in self.graph[i]:
                        m += 1
        print("Graph size is " + str(m) + " edges.")
        return m


    def order(self):
        n = len(self.graph)
        print("Graph order is " + str(n) + " verticles.")
        return n


    def clear(self):
        self.graph.clear()
        print("Graph cleared successfully.")





