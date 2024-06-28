import time


#this function is just used to get the time taken by the function to execute (Not so used as much for getting difference we can make use of it)
def timer(func):
  def wrapper_func(*args, **kwargs):
        t = time.time()
        result = func(*args, **kwargs)
        print("Time taken by {} is {} seconds.".format(func.__name__, time.time()-t))
        return result
  return wrapper_func



#BUBBLE SORT
#O(n^2) algo

@timer
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
       #swapped = False
        for j in range(0,n-i-1): #keeping reducing when more number are fixed 
            if arr[j] > arr[j+1]: #if right element is smaller then swaps
                arr[j] , arr[j+1] = arr[j+1], arr[j] # computer consider it as tuple and swap the numbers


 
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


@timer # making use of timer function to know about the time taken by the function to complete its execution
def merge_sort_wrapper(arr):
    merge_sort(arr)


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

@timer
def quick_sort_wrapper(arr):
    quick_sort(arr,0,len(arr)-1)



n = 1000 #size of the array with this value u can increase the size 
#whenever the size is too high the time taken by the bubble sort will get increased sometimes it takes minutes to complete its execution
array1 = [random.randint(1,1000) for _ in range(n)]
array2 = array1.copy()
array3 = array1.copy()


bubble_sort(array1)
#print(array1)  
merge_sort_wrapper(array2)
#print(array2)  
quick_sort_wrapper(array3)
#print(array3)