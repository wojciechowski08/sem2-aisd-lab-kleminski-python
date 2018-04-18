
from Lab3.generateArray import generate
from Lab3.algorithms.ShellSort import executeShellSort
from Lab3.algorithms.QuickSort import executeQuickSort
from Lab3.algorithms.MergeSort import executeMergeSort

import copy
import time

# cases = [50, 100, 250, 500, 1000, 2000]
cases = [100, 250, 500, 1000, 2000]

modes = ['rand', 'sort', 'half', 'rev']

# algs = ['qcksrt', 'mrgsrt', 'shllsrt']
algs = ['mrgsrt', 'shllsrt']


### VERSION 1 - PROBABLY NOT GOOD - WORKING, BUT NOT AS IT SHOULD ###
# for m in modes:
#
#     for c in cases:
#
#         for i in range(1, 100 + 1):
#             print("{} {} No. ".format(m, c) + str(i))
#
#             o = time.process_time()
#             test = generate(c * 1000)
#             oe = time.process_time() - o
#             print("Generating time: " + str(oe))
#
#             # print(test)
#
#             l = copy.copy(test)
#
#             if m == 'n':
#                 t = time.process_time()
#                 executeShellSort(l)
#                 te = time.process_time() - t
#                 # print(l)
#                 print(te)
#             elif m == 'r':
#                 t = time.process_time()
#                 executeShellSortREV(l)
#                 te = time.process_time() - t
#                 # print(l)
#                 print(te)
#             elif m == 'h':
#                 t = time.process_time()
#                 executeShellSortHALF(l)
#                 te = time.process_time() - t
#                 # print(l)
#                 print(te)
#
#
#             f = open("tests/shllsrt-{}-{}.txt".format(m, c), 'a')
#             f.write(str(te) + '\n')
#             f.close()


### VERSION 2 - GOOD - WORKING AS IT SHOULD ###

for a in algs:

    for m in modes:

        for c in cases:

            for i in range(1, 100 + 1):
                print("{} {} {} No. {}".format(a, m, c, i))

                f = open("arrays/{}-{}/{}.txt".format(m, c, i), 'r')

                array = [int(x) for x in f.readline().split()]

                f.close()

                if a == 'qcksrt':
                    t = time.process_time()
                    executeQuickSort(array)
                    te = time.process_time() - t
                    print(te)
                elif a == 'mrgsrt':
                    t = time.process_time()
                    executeMergeSort(array)
                    te = time.process_time() - t
                    print(te)
                elif a == 'shllsrt':
                    t = time.process_time()
                    executeShellSort(array)
                    te = time.process_time() - t
                    print(te)



                f = open("tests/{}-{}-{}.txt".format(a, m, c), 'a')
                f.write(str(te) + '\n')
                f.close()



