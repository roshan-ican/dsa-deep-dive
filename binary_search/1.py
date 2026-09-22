

def search(nums, target):
    left = 0
    right = len(nums) - 1

    
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1  
        else:
            right = mid - 1
    return -1
nums = [1, 3, 5, 7, 9, 11]
target = 7

print(search(nums, target))
