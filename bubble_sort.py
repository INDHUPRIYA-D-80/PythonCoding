#O(n^2) algo

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
       #swapped = False
        for j in range(0,n-i-1): #keeping reducing when more number are fixed 
            if arr[j] > arr[j+1]: #if right element is smaller then swaps
                arr[j] , arr[j+1] = arr[j+1], arr[j] # computer consider it as tuple and swap the numbers


array = [3,4,5,6,2,1,2,0]
bubble_sort(array)
print(array)  