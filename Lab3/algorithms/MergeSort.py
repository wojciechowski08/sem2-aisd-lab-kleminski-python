import copy


def executeMergeSort(data):

    def merge(left, right):
        """
        :param list left:
        :param list right:
        :return:
        """
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result


    if len(data) < 2:

        return data[:]

    else:

        middle = len(data)//2
        left = executeMergeSort(data[:middle])
        right = executeMergeSort(data[middle:])
        return merge(left, right)


def executeMergeSortREV(data):
    """

    :param list data:
    :return:
    """

    def merge(left, right):
        """
        :param list left:
        :param list right:
        :return:
        """
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result


    if len(data) < 2:

        return data[:]

    else:

        middle = len(data)//2
        left = executeMergeSortREV(data[:middle])
        right = executeMergeSortREV(data[middle:])
        return merge(left, right)


def executeMergeSortHALF(data):
    """

    :param list data:
    :return:
    """
    temp = data[len(data)//2:]
    l = copy.copy(data)
    l = executeMergeSort(l[:len(data)//2])
    data = l + temp
    return data
