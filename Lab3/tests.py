
from Lab3.generateArray import generate
from Lab3.BubbleSort import *
from Lab3.SelectionSort import *
from Lab3.MergeSort import *
from Lab3.QuickSort import *
from Lab3.ShellSort import *

import copy
import time

cases = [50, 100, 250, 500, 1000, 2000]

modes = ['n', 'h', 'r']

for m in modes:

    for c in cases:

        for i in range(1, 100 + 1):
            print("{} {} No. ".format(m, c) + str(i))

            o = time.process_time()
            test = generate(c * 1000)
            oe = time.process_time() - o
            print("Generating time: " + str(oe))

            # print(test)

            l = copy.copy(test)

            if m == 'n':
                t = time.process_time()
                executeMergeSort(l)
                te = time.process_time() - t
                # print(l)
                print(te)
            elif m == 'r':
                t = time.process_time()
                executeMergeSortREV(l)
                te = time.process_time() - t
                # print(l)
                print(te)
            elif m == 'h':
                t = time.process_time()
                executeMergeSortHALF(l)
                te = time.process_time() - t
                # print(l)
                print(te)


            f = open("tests/mrgsrt-{}-{}.txt".format(m, c), 'a')
            f.write(str(te) + '\n')
            f.close()




