import errno

from Lab3.generateArray import generate
from Lab3.algorithms.QuickSort import executeQuickSortHALF
from Lab3.algorithms.QuickSort import executeQuickSort
import os

cases = [50, 100, 250, 500, 1000, 2000]

# modes = ['n', 'r', 'h']

# algs = ['qcksrt', 'mrgsrt', 'shllsrt']


### SECTION FOR SAVING RANDOM GENERATED ARRAYS ###
### *comment if not used*                      ###

# for c in cases:
#
#     for i in range(1, 100 + 1):
#
#         if not os.path.exists(os.path.dirname("arrays/rand-{}/{}.txt".format(c, i))):
#             try:
#                 os.makedirs(os.path.dirname("arrays/rand-{}/{}.txt".format(c, i)))
#             except OSError as exc:  # Guard against race condition
#                 if exc.errno != errno.EEXIST:
#                     raise
#
#         f = open("arrays/rand-{}/{}.txt".format(c, i), 'w')
#
#         test = generate(c * 1000)
#
#         for index in range(len(test)):
#             if index == len(test) - 1:
#                 f.write(str(test[index]))
#             else:
#                 f.write(str(test[index]) + ' ')
#         f.write('\n')
#
#         # f.write(str(test) + '\n')
#
#         f.close()


### SECTION FOR SAVING HALF SORTED ARRAYS ###
### *comment if not used*                 ###

# for c in cases:
#
#     for i in range(1, 100 + 1):
#
#         f = open("arrays/rand-{}/{}.txt".format(c, i), 'r')
#
#         array = [int(x) for x in f.readline().split()]
#
#         array = executeQuickSortHALF(array)
#
#         if not os.path.exists(os.path.dirname("arrays/half-{}/{}.txt".format(c, i))):
#             try:
#                 os.makedirs(os.path.dirname("arrays/half-{}/{}.txt".format(c, i)))
#             except OSError as exc:  # Guard against race condition
#                 if exc.errno != errno.EEXIST:
#                     raise
#
#         f = open("arrays/half-{}/{}.txt".format(c, i), 'w')
#
#         for index in range(len(array)):
#             if index == len(array) - 1:
#                 f.write(str(array[index]))
#             else:
#                 f.write(str(array[index]) + ' ')
#         f.write('\n')
#
#         f.close()


### SECTION FOR SAVING FULLY SORTED ARRAYS ###
### *comment if not used*                  ###

# for c in cases:
#
#     for i in range(1, 100 + 1):
#
#         f = open("arrays/half-{}/{}.txt".format(c, i), 'r')
#
#         array = [int(x) for x in f.readline().split()]
#
#         executeQuickSort(array)
#
#         if not os.path.exists(os.path.dirname("arrays/sort-{}/{}.txt".format(c, i))):
#             try:
#                 os.makedirs(os.path.dirname("arrays/sort-{}/{}.txt".format(c, i)))
#             except OSError as exc:  # Guard against race condition
#                 if exc.errno != errno.EEXIST:
#                     raise
#
#         f = open("arrays/sort-{}/{}.txt".format(c, i), 'w')
#
#         for index in range(len(array)):
#             if index == len(array) - 1:
#                 f.write(str(array[index]))
#             else:
#                 f.write(str(array[index]) + ' ')
#         f.write('\n')
#
#         f.close()


### SECTION FOR SAVING REVERSED SORTED ARRAYS ###
### *comment if not used*                     ###

# for c in cases:
#
#     for i in range(1, 100 + 1):
#
#         f = open("arrays/sort-{}/{}.txt".format(c, i), 'r')
#
#         array = [int(x) for x in f.readline().split()]
#
#         array.reverse()
#
#         if not os.path.exists(os.path.dirname("arrays/rev-{}/{}.txt".format(c, i))):
#             try:
#                 os.makedirs(os.path.dirname("arrays/rev-{}/{}.txt".format(c, i)))
#             except OSError as exc:  # Guard against race condition
#                 if exc.errno != errno.EEXIST:
#                     raise
#
#         f = open("arrays/rev-{}/{}.txt".format(c, i), 'w')
#
#         for index in range(len(array)):
#             if index == len(array) - 1:
#                 f.write(str(array[index]))
#             else:
#                 f.write(str(array[index]) + ' ')
#         f.write('\n')
#
#         f.close()