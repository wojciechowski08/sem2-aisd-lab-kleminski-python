import time

from Lab3.algorithms.MergeSort import executeMergeSort
from Lab3.generateArray import generate
from Lab3.algorithms.ShellSort import *
from Lab3.algorithms.QuickSort import *
import copy

test = generate(20000)

print(test)

# # BUBBLE SORT ----------------------------------
# print("\nBUBBLE SORT\n")
#
# l = copy.copy(test)
# t = time.process_time()
# executeBubbleSort(l)
# te = time.process_time() - t
# print(l)
# print(te)

# k = copy.copy(test)
# executeBubbleSortREV(k)
# print(k)
#
# j = copy.copy(test)
# executeBubbleSortHALF(j)
# print(j)
#
#
# # SELECTION SORT -------------------------------
# print("\nSELECTION SORT\n")
#
# l = copy.copy(test)
# executeSelectionSort(l)
# print(l)
#
# k = copy.copy(test)
# executeSelectionSortREV(k)
# print(k)
#
# j = copy.copy(test)
# executeSelectionSortHALF(j)
# print(j)
#
#
# # MERGE SORT ----------------------------------
# print("\nMERGE SORT\n")
#
# l = copy.copy(test)
# print(executeMergeSort(l))
#
# k = copy.copy(test)
# print(executeMergeSortREV(k))
#
# j = copy.copy(test)
# print(executeMergeSortHALF(j))
#
#
# # QUICK SORT ----------------------------------
# print("\nQUICK SORT\n")
#
l = copy.copy(test)
t = time.process_time()
executeQuickSort(l)
te = time.process_time() - t
print(l)
print(te)
# executeQuickSort(l)
# print(l)
#
# k = copy.copy(test)
# executeQuickSortREV(k)
# print(k)
#
# j = copy.copy(test)
# print(executeQuickSortHALF(j))
#
#
# SHELL SORT ---------------------------------
# print("\nSHELL SORT\n")

# l = copy.copy(test)
# executeShellSort(l)
# print(l)
#
# k = copy.copy(test)
# executeShellSortREV(k)
# print(k)
#
# j = copy.copy(test)
# executeShellSortHALF(j)
# print(j)