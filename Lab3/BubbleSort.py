
def executeBubbleSort(data):
    """

    :param list data:
    :return:
    """
    size = len(data) - 1
    isSorted = False

    while not isSorted:
        isSorted = True
        for element in range(0, size):
            if data[element] >= data[element + 1]:
                isSorted = False
                temp = data[element + 1]
                data[element + 1] = data[element]
                data[element] = temp


def executeBubbleSortREV(data):
    """

    :param list data:
    :return:
    """
    size = len(data) - 1
    isSorted = False

    while not isSorted:
        isSorted = True
        for element in range(0, size):
            if data[element] <= data[element + 1]:           # only flipped comparison operator
                isSorted = False
                temp = data[element + 1]
                data[element + 1] = data[element]
                data[element] = temp


def executeBubbleSortHALF(data):
    """

    :param list data:
    :return:
    """