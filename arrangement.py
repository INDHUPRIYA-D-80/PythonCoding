def partition(arr, low, high):
    pivot = arr[high] #to separate left half and right half
    i = low-1 # i elements will be smaller,  index of left part 
    for j in range(low, high):
        if arr[j] < pivot: #condition for swapping i and j
            i+= 1
            arr[i],arr[j] = arr[j], arr[i]  #swapping
    arr[i+1], arr[high] = arr[high], arr[i+1]   # swapping elemnts of last
    return i +1



array = [-1,2,3,-4,-5,6,7,-8,9,10]
partition(array,0,len(array)-1)
print(array)