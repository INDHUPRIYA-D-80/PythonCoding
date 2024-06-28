#sorting using merge sort 

import random


def merge(arr, left_half, right_half):
    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k+=1
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1




def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2 #taking only the integer part not decimal.
        left_half = arr[:mid]  # elements before the mid are taken.
        right_half = arr[mid:] # elements after the mid are taken.

        merge_sort(left_half)
        merge_sort(right_half)
        merge(arr, left_half, right_half)
def merge_sort_wrapper(arr):
    merge_sort(arr)

n = 1000
array1 = [random.randint(1,1000) for i in range(n)]
merge_sort_wrapper(array1)
print(array1)  
