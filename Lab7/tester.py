import random

from Graph import Graph
from Simulation import Simulate

people = []
network = Graph()

# creating group of 10000 people
for person in range(200):
    people.append(person)
    network.addVertex(person)

# making connections in the group
# for edge in range(40000):
#     goodEdge = False
#     while not goodEdge:
#         p1 = random.randint(0, len(people)-1)
#         p2 = random.randint(0, len(people)-1)
#         if not p1 == p2:
#             if not (p2 in network.graph[p1] or p1 in network.graph[p2]):
#                 goodEdge = True
#     network.addEdge(p1, p2)

edges = 0
while edges <= 600:
    for person in people:
        for edge in range(1):
            goodEdge = False
            while not goodEdge:
                p = random.randint(0, len(people)-1)
                if not p == person:
                    if not (p in network.graph[person] or person in network.graph[p]):
                        goodEdge = True
            network.addEdge(p, person)
            edges += 1

print("Network created successfully.")

network.size()

# connectionStats = {}
# for person in network.graph:
#     if len(network.graph[person]) in connectionStats:
#         connectionStats[len(network.graph[person])] += 1
#     else:
#         connectionStats[len(network.graph[person])] = 1
#
# connectionStats = sorted(connectionStats.items(), key=lambda x: x[0])
# print(connectionStats)

Simulate(network, 24)

