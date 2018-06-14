from Graph import Graph

test = Graph(True, False)
for i in range(5):
    test.addVertex(i)
test.addEdge(0,1)
test.addEdge(1,2)
test.addEdge(2,3)
test.addEdge(3,4)
test.addEdge(4,0)
test.addVertex(10)
test.addEdge(10,3)
test.findStronglyConnectedComponents()
test.findCycles()

t = Graph(True, False)
for i in range(9):
    t.addVertex(i)
t.addEdge(0,1)
t.addEdge(1,2)
t.addEdge(2,5)
t.addEdge(2,4)
# t.addEdge(4,2)

t.addEdge(4,3)
# t.addEdge(3,4)
t.addEdge(5,6)
t.addEdge(6,8)
t.addEdge(6,7)
t.addEdge(7,3)
t.addEdge(3,1)
t.findStronglyConnectedComponents()
t.findCycles()