
def executeBubbleSort(data):
    """

    :param list data:
    :return:
    """
    size = len(data)
    isSorted = False

    while not isSorted:
        isSorted = True
        for i in range(1, size):
            if data[i-1] > data[i]:
                isSorted = False
                temp = data[i]
                data[i] = data[i-1]
                data[i-1] = temp


def executeBubbleSortREV(data):
    """

    :param list data:
    :return:
    """
    size = len(data)
    isSorted = False

    while not isSorted:
        isSorted = True
        for i in range(1, size):
            if data[i - 1] < data[i]:
                isSorted = False
                temp = data[i]
                data[i] = data[i - 1]
                data[i - 1] = temp


def executeBubbleSortHALF(data):
    """

    :param list data:
    :return:
    """
    size = len(data)
    isSorted = False

    while not isSorted:
        isSorted = True
        for i in range(1, size//2):
            if data[i - 1] > data[i]:
                isSorted = False
                temp = data[i]
                data[i] = data[i - 1]
                data[i - 1] = temp