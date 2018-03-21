
import random

def generate(n):
    """

    :param int n:
    :return:
    """

    list = []

    for i in range(0, n+1):

        list.append(random.randint(0, 1000000))
        # list[i] = random.randint(0, 1000000)              #cant insert at non-existing index

    return list

# test = generate(10)
# print(test[0:100])