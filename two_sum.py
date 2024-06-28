# to find the two numbers on which their sums could give the target
#NAME:two pointed technique

def two_sums(nums, target):
    nums_sorted = sorted(nums) # to get the array sorted
    left = 0   #to get started from the first
    right = len(nums_sorted)-1 #to get started from the last

    while left <right:
        current_sum = nums_sorted[left] + nums_sorted[right] #getting their sum
        if current_sum == target:  
            return (nums_sorted[left], nums_sorted[right]) #gives the element whose sum is equal to target 
        elif current_sum < target:
             left +=1 #incrementing to next element
        else:
            right -=1  #decrementing to next element  
    return -1
nums = [1,11,2,7,14,20,18]
target = 9
result=two_sums(nums,target)
print(result)