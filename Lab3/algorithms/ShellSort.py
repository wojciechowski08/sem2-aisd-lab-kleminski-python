
def executeShellSort(data):
    """

    :param list data:
    :return:
    """
    # n = len(data)
    # h = 1
    # while h >= n:
    #     h = h*3 + 1
    # h = h//9
    # if h == 0:
    #     h = 1
    # while h > 0:
    #     for j in range(n-h, 1, -1):
    #         x = data[j]
    #         i = j + h
    #         while i <= n and x > data[i]:
    #             data[i-h] = data[i]
    #             i = i + h
    #         data[i-h] = x
    #     h = h//3

    gap = len(data) // 2
    # loop over the gaps
    while gap > 0:
        # do the insertion sort
        for i in range(gap, len(data)):
            val = data[i]
            j = i
            while j >= gap and data[j - gap] > val:
                data[j] = data[j - gap]
                j -= gap
            data[j] = val
        gap //= 2


def executeShellSortREV(data):
    """

    :param list data:
    :return:
    """

    gap = len(data) // 2
    # loop over the gaps
    while gap > 0:
        # do the insertion sort
        for i in range(gap, len(data)):
            val = data[i]
            j = i
            while j >= gap and data[j - gap] < val:
                data[j] = data[j - gap]
                j -= gap
            data[j] = val
        gap //= 2


def executeShellSortHALF(data):
    """

    :param list data:
    :return:
    """

    gap = len(data) // 4
    # loop over the gaps
    while gap > 0:
        # do the insertion sort
        for i in range(gap, len(data)//2):
            val = data[i]
            j = i
            while j >= gap and data[j - gap] > val:
                data[j] = data[j - gap]
                j -= gap
            data[j] = val
        gap //= 2