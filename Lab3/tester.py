
from generateArray import generate
from BubbleSort import *
from SelectionSort import *
import copy

test = generate(20)

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