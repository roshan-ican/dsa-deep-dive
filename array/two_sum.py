def twoSum(nums, target):
    map = {}
    for i in range(len(nums) - 1):
        s = nums[i] + nums[i + 1]
        if s == target:
            return [i, i + 1]
        complacent = abs(target - nums[i])
        if complacent in map:
            found = [map[complacent], i]
            return found
        map[nums[i]] = i
    


nums, target = [3,4,5,6],  8

print(twoSum(nums, target))

# Output: [0,1]