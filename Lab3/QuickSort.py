
def executeQuickSort(data):
    """

    :param list data:
    :return:
    """

    def helper(data, first, last):
        if first < last:
            splitpoint = partition(data, first, last)

            helper(data, first, splitpoint - 1)
            helper(data, splitpoint + 1, last)

    def partition(data, first, last):
        pivotvalue = data[first]

        leftmark = first + 1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and data[leftmark] <= pivotvalue:
                leftmark = leftmark + 1

            while data[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1

            if rightmark < leftmark:
                done = True
            else:
                temp = data[leftmark]
                data[leftmark] = data[rightmark]
                data[rightmark] = temp

        temp = data[first]
        data[first] = data[rightmark]
        data[rightmark] = temp

        return rightmark

    helper(data, 0, len(data) - 1)


def executeQuickSortREV(data):
    """

    :param list data:
    :return:
    """
    def helper(data, first, last):
        if first < last:
            splitpoint = partition(data, first, last)

            helper(data, first, splitpoint - 1)
            helper(data, splitpoint + 1, last)

    def partition(data, first, last):
        pivotvalue = data[first]

        leftmark = first + 1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and data[leftmark] >= pivotvalue:
                leftmark = leftmark + 1

            while data[rightmark] <= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1

            if rightmark < leftmark:
                done = True
            else:
                temp = data[leftmark]
                data[leftmark] = data[rightmark]
                data[rightmark] = temp

        temp = data[first]
        data[first] = data[rightmark]
        data[rightmark] = temp

        return rightmark

    helper(data, 0, len(data) - 1)


# def executeQuickSortHALF(data):
#     """
#
#     :param list data:
#     :return:
#     """





