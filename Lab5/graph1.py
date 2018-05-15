import random

from Graph import Graph

g = Graph(True, True)
for i in range(15):
    g.addVertex()
g.order()
weights = []
for j in range(23):
    o = random.randint(1, 30)
    weights.append(o)
print(weights)
g.addEdge(0,1,2)#0
g.addEdge(0,2,7)
g.addEdge(1,0,2)#1
g.addEdge(1,2,25)
g.addEdge(2,0,7)#2
g.addEdge(2,3,25)
g.addEdge(3,2,25)
g.addEdge(3,4,29)
g.addEdge(3,8,5)
g.addEdge(4,3,28)#4
g.addEdge(4,5,1)
g.addEdge(4,9,17)
g.addEdge(5,4,1)#5
g.addEdge(5,10,24)
g.addEdge(6,1,5)#6
g.addEdge(6,7,23)
g.addEdge(7,6,23)#7
g.addEdge(8,3,5)#8
g.addEdge(8,4,17)
g.addEdge(8,12,28)
g.addEdge(9,4,17)#9
g.addEdge(9,8,26)
g.addEdge(9,12,11)
g.addEdge(9,13,29)
g.addEdge(10,5,24)#10
g.addEdge(10,13,2)
g.addEdge(11,7,22)#11
g.addEdge(11,9,4)
g.addEdge(12,8,28)#12
g.addEdge(12,11,23)
g.addEdge(13,10,2)#13
g.addEdge(13,14,30)
g.addEdge(14,13,30)
g
