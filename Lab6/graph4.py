from Graph import Graph

test = Graph(True, False)
for i in range(4):
    test.addVertex(i)
test.addEdge(0,1)
test.addEdge(1,2)
test.addEdge(2,3)
test.addEdge(3,0)
test.addVertex(4)
test.addEdge(4,3)
test.findStronglyConnectedComponents()
test.findCycles()