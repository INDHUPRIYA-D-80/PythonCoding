def find_peak(arr):
    low = 0 
    high = len(arr)-1

    while low < high:
        mid = (low+high)//2

        if  arr[mid] == arr[mid+1]:
            high = mid
        else:
            low = mid+1
    return low
array = [1,3,7,20,17,4,2,1]

peak_index = find_peak(array)

peak_element = array[peak_index]
print(peak_index)