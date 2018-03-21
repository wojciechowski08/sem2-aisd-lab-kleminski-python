
def executeSelectionSort(data):
    """

    :param list data:
    :return:
    """
    size = len(data)
    suffix = 0

    while suffix != size:

        for i in range(suffix, size):

            if data[i] < data[suffix]:

                data[suffix], data[i] = data[i], data[suffix]

        suffix += 1



def executeSelectionSortREV(data):
    """

    :param list data:
    :return:
    """
    size = len(data)
    suffix = 0

    while suffix != size:

        for i in range(suffix, size):

            if data[i] > data[suffix]:
                data[suffix], data[i] = data[i], data[suffix]

        suffix += 1


def executeSelectionSortHALF(data):
    """

    :param list data:
    :return:
    """
    size = len(data)
    suffix = 0

    while suffix != size:

        for i in range(suffix, size//2):

            if data[i] < data[suffix]:
                data[suffix], data[i] = data[i], data[suffix]

        suffix += 1