#PS arrange the sorted array in even odd pattern


def partition(arr, low, high):
    i = low-1 # i elements will be smaller,  index of left part
    for j in range(low, high):
        if arr[j]%2 != 0: #condition for swapping i and j (to print first as even and next as odd)
            i+= 1
            arr[i],arr[j] = arr[j], arr[i]  #swapping
    arr[i+1], arr[high] = arr[high], arr[i+1]   # swapping elemnts of last
    return i +1

	 
def alternate_odd_even(arr):
    n = len(arr)//2
    pivot_index = partition(arr, 0, len(arr)-1)
    pos_idx = n
    neg_idx = 0
    while pos_idx < 2*n and neg_idx < n:
        arr[pos_idx], arr[neg_idx] = arr[neg_idx], arr[pos_idx]
        pos_idx += 2
        neg_idx += 2
    return arr
	 
array = [3, 4, 1, 1, 6, 8, 10, 11, 9, 10]
print(alternate_odd_even(array))
