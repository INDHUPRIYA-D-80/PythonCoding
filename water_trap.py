def trap(height):
    n = len(height)
    if n <= 2:
        return 0

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    trapped_water = 0
    for i in range(n):
        trapped_water += max(min(left_max[i], right_max[i]) - height[i], 0)


    return trapped_water

# Example usage:
pillar_heights = [3,0,1,5,2,4]
result = trap(pillar_heights)
print("Amount of trapped water:", result)
