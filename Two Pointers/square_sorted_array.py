nums = [-4, -1, 0, 3, 10]
n = len(nums)
left = 0
right = n-1
result = [0] * n
index = n-1

while left <= right:
    if abs(nums[left]) > abs(nums[right]):
        result[index] = nums[left] ** 2
        left += 1
    
    else:
        result[index] = nums[right] ** 2
        right -= 1
    index -= 1

print(result)