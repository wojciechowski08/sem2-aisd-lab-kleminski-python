import sys


class Graph:


    def __init__(self, isDirected=True, isWeighted=False):

        self.isDirected = isDirected
        self.isWeighted = isWeighted

        # self.verticles
        # self.edges
        self.adjacencyList = []
        self.weights = {}
        self.values = {}


    # works for Directed and non-Directed
    def addVertex(self, vertex=None):
        if vertex == None:
            self.adjacencyList.append([])
            print("Vertex " + str(len(self.adjacencyList) - 1) + " added to graph.")
        # elif self.adjacencyList[vertex] != None




    # works for Directed and non-Directed
    # works for Weighted and non-Weighted
    # not working coz changes next verticles
    def removeVertex(self, vert):
        try:
            self.adjacencyList.pop(vert)
            # self.adjacencyList[vert] = None
            if len(self.adjacencyList) != 0:
                for i in self.adjacencyList:
                    try:
                        i.remove(vert)
                        del self.weights["{}-{}".format(vert, self.adjacencyList.index(i))]
                        del self.weights["{}-{}".format(self.adjacencyList.index(i), vert)]
                    except KeyError:
                        True
                print("Vertex " + str(vert) + " removed from graph.")
        except IndexError:
            print("Could not remove non-existing vertex " + str(vert) + ".")


    # works for Directed and non-Directed
    # works for Weighted and non-Weighted
    def addEdge(self, vert1, vert2, weight=1):

        try:
            if vert2 in range(len(self.adjacencyList)):
                (self.adjacencyList[vert1]).append(vert2)
                self.weights['{}-{}'.format(vert1, vert2)] = weight
                if not self.isDirected:
                    (self.adjacencyList[vert2]).append(vert1)
                    self.weights['{}-{}'.format(vert2, vert1)] = weight
                print("Edge between " + str(vert1) + " and " + str(vert2) + " added succesfully.")
            else:
                print("Could not add edge, missing " + str(vert2) + " vertex.")
        except ValueError:
            print("Could not add edge, missing " + str(vert1) + " vertex.")


    # works for Directed and non-Directed
    def removeEdge(self, vert1, vert2):

        try:
            if vert2 in self.adjacencyList[vert1]:
                (self.adjacencyList[vert1]).remove(vert2)
                del self.weights['{}-{}'.format(vert1, vert2)]
                if not self.isDirected:
                    (self.adjacencyList[vert2]).remove(vert1)
                    del self.weights['{}-{}'.format(vert2, vert1)]
                print("Edge between " + str(vert1) + " and " + str(vert2) + " removed succesfully.")
            else:
                print("Could not remove edge, missing " + str(vert2) + " vertex.")

        except ValueError:

            print("Could not remove edge, missing " + str(vert1) + " vertex.")


    # def setVertexValue(self):
    #
    #     print()


    # works for Directed and non-Directed
    # works for Weighted and non-Weighted
    def setEdgeWeight(self, vert1, vert2, weight):
        if self.isWeighted:
            try:
                self.weights["{}-{}".format(vert1, vert2)] = weight
                if not self.isDirected:
                    self.weights["{}-{}".format(vert2, vert1)] = weight
                print("Edge weight changed to " + str(weight) + " succesfully.")
            except KeyError:
                print("No such edge in graph.")
        else:
            print("This graph is not weighted.")


    # works for Directed and non-Directed
    # works for Weighted and non-Weighted
    def viewVerticles(self):
        if len(self.adjacencyList) != 0:
            verts = ""
            for i in range(len(self.adjacencyList)):
                verts += str(i) + " "
            print(verts)
        else:
            print("No verticles.")


    # works for Directed and non-Directed
    # works for Weighted and non-Weighted
    def viewEdges(self):
        if len(self.adjacencyList) != 0:
            edges = ""
            for i in range(len(self.adjacencyList)):
                if len(self.adjacencyList[i]) != 0:
                    for j in self.adjacencyList[i]:
                        if self.isWeighted:
                            edges += str(i) + " --- " + str(j) + " : " + str(self.weights["{}-{}".format(i, j)]) + "\n"
                        else:
                            edges += str(i) + " --- " + str(j) + "\n"
            if edges == "":
                print("No edges between verticles.")
            else:
                print(edges)
        else:
            print("No verticles, so no edges.")


    def degree(self, vertex):

        both = 0
        inWay = 0
        outWay = 0
        for i in range(len(self.adjacencyList)):
            for j in self.adjacencyList[i]:
                if i == vertex:
                    outWay += 1
                    both += 1
                try:
                    if (self.adjacencyList[i])[j] == vertex:
                        inWay += 1
                        both += 1
                except IndexError:
                    True
        if self.isDirected:
            print("Vertex " + str(vertex) + " has degree of " + str(both) +
                  " (" + str(outWay) + " edges out, " + str(inWay) + " edges in).")
        else:
            print("Vertex " + str(vertex) + " has degree of " + str(both//2) + ".")


    # works for Directed and non-Directed
    # works for Weighted and non-Weighted
    def viewNeighbours(self, vertex):
        neighbours = ""
        for i in self.adjacencyList[vertex]:
            neighbours += str(i) + " "
        print("Neighbours for vertex " + str(vertex) + ": " + neighbours)


    # def findMinSpanningTree(self):
    #################################################################################################################


    # not working
    def findShortestPath(self, vert1, vert2):

        # n = self.order()
        # d = []
        # p = []
        # v = vert1
        # for i in range(n):
        #     d.append(sys.maxsize)
        #     p.append(-1)
        # d[v] = 0
        # for i in range(1, n+1):
        #     test = True
        #     for x in range(0, n):
        #         for y in self.adjacencyList[x]:
        #             if d[y] <= d[x] + self.weights["{}-{}".format(x, y)]:
        #                 test = False
        #                 d[y] = d[x] + self.weights["{}-{}".format(x, y)]
        #                 p[y] = x
        #     if test:
        #         return True
        # for x in range(0, n):
        #     for y in self.adjacencyList[x]:
        #         if d[y] > d[x] + self.weights["{}-{}".format(x, y)]:
        #             print(d)
        #             print(p)
        #             return False
        #
        # return True

        n = self.order()
        v = vert1
        d = []
        p = []
        for i in range(n):
            d.append(sys.maxsize)
            p.append(-1)





    def size(self):

        m = 0
        if len(self.adjacencyList) != 0:
            for i in range(len(self.adjacencyList)):
                if len(self.adjacencyList[i]) != 0:
                    for j in self.adjacencyList[i]:
                        m += 1
        print("Graph size is " + str(m) + " edges.")
        return m


    # works for Directed and non-Directed
    # works for Weighted and non-Weighted
    def order(self):

        n = len(self.adjacencyList)
        print("Graph order is " + str(n) + " verticles.")
        return n





