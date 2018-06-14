import random

from Graph import Graph

def Simulate(network: Graph, hours=24, probFNF=66.6, probFNT=2.5, probFTF=2, probTNT=80, probTNF=5, probTFT=50, rootFakeInfo=8, delayTrueInfo=4):

    # timePassed = 0
    notKnowing = len(network.status) - 1 # -1 because of 1 infected person
    knowsFake = 1
    knowsTruth = 0

    (network.status[ random.randint(0, len(network.status)) ])[0] = -1   # setting 1 infected
    # (network.status[random.randint(0, len(network.status))])[1] = 1     #setting 1 hour for infected

    # time passing
    for h in range(hours):

        # checking all people
        for person in network.status:

            # if is infected
            if (network.status[person])[0] == -1:

                # if required time has passed
                if (network.status[person])[1] > 0:

                    # checking all friends
                    for friend in network.graph[person]:

                        # if friend didn't heard about info at all
                        if (network.status[friend])[0] == 0:

                            # probability of believing in fake info = 2/3
                            if random.randint(0,100) < probFNF:

                                # friend believes in fake info
                                (network.status[friend])[0] = -1
                                # set time at current status to 0
                                (network.status[friend])[1] = 0
                                notKnowing -= 1
                                knowsFake += 1

                            # probability of believing in truth = 2.5%
                            elif random.randint(0,100) < probFNT and h > delayTrueInfo:

                                # friend finds out true info
                                (network.status[friend])[0] = 1
                                # set time at current status to 0
                                (network.status[friend])[1] = 0
                                notKnowing -= 1
                                knowsTruth += 1

                        # if friend knows truth
                        elif (network.status[friend])[0] == 1:

                            # probability of believing in fake info = 2%
                            if (random.randint(0, 100) <= probFTF):
                                # friend believes in fake info
                                (network.status[friend])[0] = -1
                                # set time at current status to 0
                                (network.status[friend])[1] = 0
                                knowsTruth -= 1
                                knowsFake += 1


            # if knows the truth
            elif (network.status[person])[0] == 1:

                # if required time has passed
                if (network.status[person])[1] > 0:

                    # checking all friends
                    for friend in network.graph[person]:

                        # if friend didn't heard about info at all
                        if (network.status[friend])[0] == 0:

                            # probability of believing in truth  = 80%
                            if (random.randint(0, 100) <= probTNT):
                                # friend believes in fake info
                                (network.status[friend])[0] = 1
                                # set time at current status to 0
                                (network.status[friend])[1] = 0
                                notKnowing -= 1
                                knowsTruth += 1

                            # probability of not believing in truth = 5
                            elif (random.randint(0, 100) <= probTNF):
                                # friend believes in fake info
                                (network.status[friend])[0] = -1
                                # set time at current status to 0
                                (network.status[friend])[1] = 0
                                notKnowing -= 1
                                knowsFake += 1

                        # if friend believes in fake info
                        elif (network.status[friend])[0] == -1:

                            # if friend knows fake for long time
                            if (network.status[friend])[1] > rootFakeInfo:
                                pass

                            # probability of believing in truth  = 1/2
                            elif (random.randint(0, 100) <= probTFT):
                                # friend believes in fake info
                                (network.status[friend])[0] = 1
                                # set time at current status to 0
                                (network.status[friend])[1] = 0
                                knowsFake -= 1
                                knowsTruth += 1



        # dodawanie godziny do obecnego statusu ludzi
        for person in network.status:
            (network.status[person])[1] += 1

        print("Stats after " + str(h+1) + "h:" +
              "\t\tNot Knowing:" + str(notKnowing) +
              "\t\tKnowing Fake: " + str(knowsFake) +
              "\t\tKnowing Truth: " + str(knowsTruth))


def RUN(nPeople: int, nConnections: int, maxCPP: int, time: int, probFNF=66.6, probFNT=2.5, probFTF=2, probTNT=80, probTNF=5, probTFT=50, rootFakeInfo=8, delayTrueInfo=4):

    people = []
    network = Graph()

    # creating group of nPeople people
    for person in range(nPeople):
        people.append(person)
        network.addPerson(person)

    # making connections in the group
    for edge in range(nConnections):

        # helping variables
        goodEdge = False
        failCounter = 0

        while not goodEdge:

            # picking 2 random people
            p1 = random.randint(0, len(people) - 1)
            p2 = random.randint(0, len(people) - 1)

            # checking if not same person
            if not p1 == p2:

                # checking if connection doesn't exist yet
                if not (p2 in network.graph[p1] or p1 in network.graph[p2]):

                    # checking if max connections per person not reached
                    if len(network.graph[p1]) <= maxCPP:
                        # good to go
                        goodEdge = True

            # if one of checkers failed
            failCounter += 1
            if failCounter > 1000:
                failCounter = 0
                break

        # add connection to the network
        network.addConnection(p1, p2)

    print("Network created successfully.")

    Simulate(network, time, probFNF, probFNT, probFTF, probTNT, probTNF, probTFT, rootFakeInfo, delayTrueInfo)



# connectionStats = {}
# for person in network.graph:
#     if len(network.graph[person]) in connectionStats:
#         connectionStats[len(network.graph[person])] += 1
#     else:
#         connectionStats[len(network.graph[person])] = 1
#
# connectionStats = sorted(connectionStats.items(), key=lambda x: x[0])
# print(connectionStats)