
from Lab3.generateArray import generate
from Lab3.BubbleSort import *
from Lab3.SelectionSort import *
from Lab3.MergeSort import *
from Lab3.QuickSort import *
import copy


test = generate(10)

print(test)

# BUBBLE SORT ----------------------------------
print("\nBUBBLE SORT\n")

l = copy.copy(test)
executeBubbleSort(l)
print(l)

k = copy.copy(test)
executeBubbleSortREV(k)
print(k)

j = copy.copy(test)
executeBubbleSortHALF(j)
print(j)


# SELECTION SORT -------------------------------
print("\nSELECTION SORT\n")

l = copy.copy(test)
executeSelectionSort(l)
print(l)

k = copy.copy(test)
executeSelectionSortREV(k)
print(k)

j = copy.copy(test)
executeSelectionSortHALF(j)
print(j)


# MERGE SORT ----------------------------------
print("\nMERGE SORT\n")

l = copy.copy(test)
print(executeMergeSort(l))

k = copy.copy(test)
print(executeMergeSortREV(k))

j = copy.copy(test)
print(executeMergeSortHALF(j))


# QUICK SORT ----------------------------------
print("\nQUICK SORT\n")

l = copy.copy(test)
executeQuickSort(l)
print(l)

k = copy.copy(test)
executeQuickSortREV(k)
print(k)

j = copy.copy(test)
print(executeQuickSortHALF(j))