import datetime
from enum import Enum
import random

# Sort Types
class SortType(Enum):
    BUBBLE_SORT = "Bubble Sort"
    INSERTION_SORT = "Insertion Sort"
    SELECTION_SORT = "Selection Sort"
    COUNT_SORT = "Count Sort"
    MERGE_SORT = "Merge Sort"
    QUICK_SORT = "Quick Sort"

# Keep testing arrays persistence for true benchmark between sort types
testing_arrays = {
    100: list(range(0, 100)),
    1000: list(range(0, 1000)),
    10000: list(range(0, 10000)),
    100000: list(range(0, 100000)),
    1000000: list(range(0, 1000000))
}

for arr in testing_arrays.values():
    random.shuffle(arr)

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = 1
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def mergeSort(arr, l=None, r=None):
    if l is None:
        l = 0
    if r is None:
        r = len(arr)-1

    if l < r:
        m = int((l+(r-1))/2)
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        mergeSortMerge(arr, l, m, r)

    return arr

def mergeSortMerge(arr, l, m, r):
    n1 = int(m - l + 1)
    n2 = int(r - m)

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l+i]
    for j in range(0, n2):
        R[j] = arr[m+1+j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def quickSort(arr, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(arr)-1

    if low < high:
        partitionIndex = quickSortPartition(arr, low, high)
        quickSort(arr, low, partitionIndex-1)
        quickSort(arr, partitionIndex+1, high)

def quickSortPartition(arr, low, high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def countSort(arr, max_val=None):
    if max_val is None:
        max_val = arr[0]
        for item in arr:
            if item > max_val:
                max_val = item
    m = max_val + 1
    count = [0]*m
    for a in arr:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            arr[i] = a
            i += 1
    return arr

def bubbleSort(arr):
    total = len(arr)

    for i in range(total):
        for j in range(0, total-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

def calculateSort(sortType, arr):
    print("Testing", sortType.value, "for", len(arr), "values")
    start = datetime.datetime.now()

    if sortType is SortType.INSERTION_SORT:
        insertionSort(arr[:])
    elif sortType is SortType.SELECTION_SORT:
        selectionSort(arr[:])
    elif sortType is SortType.MERGE_SORT:
        mergeSort(arr[:])
    elif sortType is SortType.QUICK_SORT:
        quickSort(arr[:])
    elif sortType is SortType.COUNT_SORT:
        countSort(arr[:])
    elif sortType is SortType.BUBBLE_SORT:
        bubbleSort(arr[:])

    end = datetime.datetime.now()
    print("Finished in", (end-start).total_seconds(), "seconds!")

for sortType in SortType:
    for array in testing_arrays.values():
        calculateSort(sortType, array)
