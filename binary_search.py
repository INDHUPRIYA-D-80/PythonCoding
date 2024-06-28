def binary_search(arr,target):
    low = 0 
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2

        if  arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid -1
        else:
            high = mid-1
    return -1
array = [11,20,33,40,55,60,77,80,99,101,203,506,709]

print(binary_search(array,99))
print(binary_search(array,0))
print(binary_search(array,4))
print(binary_search(array,203))
print(binary_search(array,709))
