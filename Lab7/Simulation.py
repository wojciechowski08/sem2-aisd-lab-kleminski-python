import random

from Graph import Graph

def Simulate(network: Graph,hours : int, ):

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
                            if random.randint(0,100) < 66.6:

                                # friend believes in fake info
                                (network.status[friend])[0] = -1
                                # set time at current status to 0
                                (network.status[friend])[1] = 0
                                notKnowing -= 1
                                knowsFake += 1

                            # probability of believing in truth = 2.5%
                            elif random.randint(0,100) < 2.5:

                                # friend finds out true info
                                (network.status[friend])[0] = 1
                                # set time at current status to 0
                                (network.status[friend])[1] = 0
                                notKnowing -= 1
                                knowsTruth += 1

                        # if friend knows truth
                        elif (network.status[friend])[0] == 1:

                            # probability of believing in fake info = 2%
                            if (random.randint(0, 100) <= 2):
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

                            # probability of believing in truth  = 4/5
                            if (random.randint(0, 100) <= 80):
                                # friend believes in fake info
                                (network.status[friend])[0] = 1
                                # set time at current status to 0
                                (network.status[friend])[1] = 0
                                notKnowing -= 1
                                knowsTruth += 1

                        # if friend believes in fake info
                        elif (network.status[friend])[0] == -1:

                            # if friend knows fake for long time
                            if (network.status[friend])[1] > 8:
                                pass

                            # probability of believing in truth  = 1/2
                            elif (random.randint(0, 100) <= 50):
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
