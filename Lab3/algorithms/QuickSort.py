import copy


def executeQuickSort(data):
    """

    :param list data:
    :return:
    """


    # def helper(data, first, last):
    #     tempStack = []
    #     tempStack.append((first, last))
    #     while tempStack:
    #         pos = tempStack.pop()
    #         last, first = pos[1], pos[0]
    #         piv = partition(data,first,last)
    #         if piv-1 > first:
    #             tempStack.append((first,piv-1))
    #         if piv+1 < last:
    #             tempStack.append((piv+1,last))

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


def executeQuickSortHALF(data):
    """

    :param list data:
    :return:
    """
    temp = data[len(data) // 2:]
    l = copy.copy(data)
    l = l[:len(data)//2]
    executeQuickSort(l)
    result = l + temp
    return result





