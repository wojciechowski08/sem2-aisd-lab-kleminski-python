import operator
import sys


class Graph:

    def __init__(self, isDirected=True, isWeighted=False):
        """
        Creates graph data structure. Built out of verticles, and edges.
        Every vertex has its own unique name which can be string, integer or float.
        Edges have weight which is set = 1 by default, and can be directed or non-directed.
        :param bool isDirected:
        :param bool isWeighted:
        """
        self.isDirected = isDirected
        self.isWeighted = isWeighted

        # self.verticles
        # self.edges
        self.graph = {}
        self.weights = {}
        # self.values = {}



    def addVertex(self, vertex):
        """

        :param vertex:
        :return:
        """
        if not vertex in self.graph:
            self.graph[vertex] = []
            print("Vertex " + str(vertex) + " added to graph.")
        else:
            print(str(vertex) + " already in graph, try different name.")



    def removeVertex(self, vert):
        """

        :param name vert:
        :return:
        """
        try:
            del self.graph[vert]
            if len(self.graph) != 0:
                for i in self.graph:
                    try:
                        self.graph[i].remove(vert)
                        del self.weights["{}-{}".format(vert, i)]
                        del self.weights["{}-{}".format(i, vert)]
                    except KeyError:
                        True
                print("Vertex " + str(vert) + " removed from graph.")
        except KeyError:
            print("Could not remove non-existing vertex " + str(vert) + ".")



    def addEdge(self, vert1, vert2, weight=1):

        if vert1 in self.graph and vert2 in self.graph:
            (self.graph[vert1]).append(vert2)
            self.weights['{}-{}'.format(vert1, vert2)] = weight
            if not self.isDirected:
                (self.graph[vert2]).append(vert1)
                self.weights['{}-{}'.format(vert2, vert1)] = weight
            print("Edge between " + str(vert1) + " and " + str(vert2) + " added succesfully.")
        else:
            print("Could not add edge, missing vertex.")



    def removeEdge(self, vert1, vert2):

        try:
            if vert2 in self.graph[vert1]:
                (self.graph[vert1]).remove(vert2)
                del self.weights['{}-{}'.format(vert1, vert2)]
                if not self.isDirected:
                    (self.graph[vert2]).remove(vert1)
                    del self.weights['{}-{}'.format(vert2, vert1)]
                print("Edge between " + str(vert1) + " and " + str(vert2) + " removed succesfully.")
            else:
                print("Could not remove edge, missing " + str(vert2) + " vertex.")

        except KeyError:

            print("Could not remove edge, missing " + str(vert1) + " vertex.")



    def setVertexName(self, vertex, newName):

        if vertex in self.graph:
            temp = self.graph[vertex]
            self.graph[newName] = temp
            del self.graph[vertex]
            if len(self.graph) != 0:
                for i in self.graph:
                    if vertex in self.graph[i]:
                        self.graph[i].remove(vertex)
                        self.graph[i].append(newName)
                        temp = self.weights["{}-{}".format(vertex, i)]
                        self.weights["{}-{}".format(newName, i)] = temp
                        del self.weights["{}-{}".format(vertex, i)]
                        if not self.isDirected:
                            temp = self.weights["{}-{}".format(i, vertex)]
                            self.weights["{}-{}".format(i, newName)] = temp
                            del self.weights["{}-{}".format(i, vertex)]
                print("Vertex name changed from " + str(vertex) + " to" + str(newName) + ".")
        else:
            print("Could not change name for non-existing vertex " + str(vertex) + ".")



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
        for i in self.graph:
            for j in self.graph[i]:
                if i == vertex:
                    outWay += 1
                    both += 1
                try:
                    if (self.graph[i])[j] == vertex:
                        inWay += 1
                        both += 1
                except IndexError:
                    True
        if self.isDirected:
            print("Vertex " + str(vertex) + " has degree of " + str(both) +
                  " (" + str(outWay) + " edges out, " + str(inWay) + " edges in).")
        else:
            print("Vertex " + str(vertex) + " has degree of " + str(both//2) + ".")



    def viewNeighbours(self, vertex):
        if vertex in self.graph:
            neighbours = ""
            for i in self.graph[vertex]:
                neighbours += str(i) + " "
            print("Neighbours for vertex " + str(vertex) + ": " + neighbours)
        else:
            print("No such vertex in the graph.")



    def findMinSpanningTree(self):

        def sortDict(dict):
            tempL = []
            newDict = {}
            for key, value in dict.items():
                tempL.append([value, key])
                tempL.sort()
            for i in tempL:
                newDict[i[1]] = i[0]
            return newDict

        Z = []

        def findSet(vert):
            for i in Z:
                if vert in i:
                    return i

        n = self.order()
        Q = sortDict(self.weights)
        T = {}

        for v in self.graph.keys():
            Z.append({str(v)})
        for i in range(n-1):
            temp = {}
            temp[list(Q.keys())[0]] = Q[list(Q.keys())[0]]
            del Q[list(Q.keys())[0]]
            tempVertexName = (list(temp.keys())[0]).split("-")
            while findSet(tempVertexName[0]) == findSet(tempVertexName[1]):
                temp = {}
                temp[list(Q.keys())[0]] = Q[list(Q.keys())[0]]
                del Q[list(Q.keys())[0]]
                tempVertexName = (list(temp.keys())[0]).split("-")
            T.update(temp)
            Z.append((findSet(tempVertexName[0])).union(findSet(tempVertexName[1])))
            Z.remove(findSet(tempVertexName[0]))
            Z.remove(findSet(tempVertexName[1]))
        return T



    def findShortestPath(self, vert1, vert2):

        n = self.order()
        d = {}
        p = {}
        v = vert1
        S = []
        Q = list(self.graph.keys())
        for i in self.graph:
            d[i] = sys.maxsize
            p[i] = None
        d[v] = 0
        while not len(Q) == 0:
            min = sys.maxsize
            for i in d.keys():
                if i in Q:
                    if d[i] <= min:
                        u = i
                        min = d[i]
            S.append(u)
            Q.remove(u)
            for w in self.graph[u]:
                if not w in Q:
                    continue
                if d[w] > d[u] + self.weights["{}-{}".format(u,w)]:
                    d[w] = d[u] + self.weights["{}-{}".format(u,w)]
                    p[w] = u

        current = vert2
        next = p[current]
        pathStr = ""
        path = []
        while not next == None:
            path.append(current)
            current = next
            next = p[current]
        path.append(current)
        path.reverse()
        for i in path:
            pathStr += str(i) + " --- "
        pathStr = pathStr[:-5]
        print("Path from vertex " + str(vert1) + " to vertex " + str(vert2) + ": " + pathStr)
        print("Overall weight: " + str(d[vert2]))



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
        self.weights.clear()
        print("Graph cleared successfully.")



    def findStronglyConnectedComponents(self):

        def transposition():
            tempAdjacencyList = {}
            for i in list(self.graph.keys()):
                tempAdjacencyList[i] = []
            for v in self.graph:
                for u in self.graph[v]:
                    tempAdjacencyList[u].append(v)
            return tempAdjacencyList

        def DFSstack(v, visited, S):
            visited[v] = True
            for u in self.graph[v]:
                if not visited[u]:
                    DFSstack(u, visited, S)
            S.append(v)

        def DFSprint(v, visited, graph):
            visited[v] = True
            # print(v)
            for u in graph[v]:
                if not visited[u]:
                    DFSprint(u, visited, graph)
            print(v)

        visited = {}
        for i in self.graph:
            visited[i] = False
        S = []
        for v in self.graph:
            if not visited[v]:
                DFSstack(v, visited, S)
        tempGraph = transposition()
        for i in tempGraph:
            visited[i] = False
        cn = 0
        while len(S) != 0:
            v = S.pop()
            if visited[v]:
                continue
            cn += 1
            print("SCC", str(cn), ":")
            DFSprint(v, visited, tempGraph)



    def findCycles(self):

        def transposition():
            tempAdjacencyList = {}
            for i in list(self.graph.keys()):
                tempAdjacencyList[i] = []
            for v in self.graph:
                for u in self.graph[v]:
                    tempAdjacencyList[u].append(v)
            return tempAdjacencyList

        def DFSstack(v, visited, S):
            visited[v] = True
            for u in self.graph[v]:
                if not visited[u]:
                    DFSstack(u, visited, S)
            S.append(v)

        def DFSprint(v, visited, graph):
            visited[v] = True
            # print(v)
            for u in graph[v]:
                if not visited[u]:
                    # DFSprint(u, visited, graph)
                    return DFSprint(u, visited, graph) + [v]
            return [v]

        visited = {}
        for i in self.graph:
            visited[i] = False
        S = []
        for v in self.graph:
            if not visited[v]:
                DFSstack(v, visited, S)
        tempGraph = transposition()
        for i in tempGraph:
            visited[i] = False
        cn = 1
        while len(S) != 0:
            v = S.pop()
            if visited[v]:
                continue

            t = DFSprint(v, visited, tempGraph)
            if len(t) > 1:
                print("Cycle", str(cn), ":")
                print(t)
                cn += 1






