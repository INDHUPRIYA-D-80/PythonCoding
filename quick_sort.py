#QUICK SORT
import random
def partition(arr, low, high):
    pivot = arr[high] #to separate left half and right half
    i = low-1 # i elements will be smaller,  index of left part
    for j in range(low, high):
        if arr[j] < pivot: #condition for swapping i and j
            i+= 1
            arr[i],arr[j] = arr[j], arr[i]  #swapping
    arr[i+1], arr[high] = arr[high], arr[i+1]   # swapping elemnts of last
    return i +1


def quick_sort(arr, low, high):
    if low < high: 
        pivot_index = partition(arr,low, high)

        quick_sort(arr, low, pivot_index-1)
        quick_sort(arr,pivot_index+1,high)


def quick_sort_wrapper(arr):
    quick_sort(arr,0,len(arr)-1)


#array = [3,3,4,5,6,2,1,2,0]
n = 1000
array1 = [random.randint(1,1000) for _ in range(n)]
quick_sort_wrapper(array1)
print(array1)
