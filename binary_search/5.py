nums, target = [5, 7, 7, 8, 8, 10], 8
# Output: [3,4]


def FindPArray(nums, target):
    lo = 0
    hi = len(nums) - 1
    res = [-1, -1]

    # find first position
    while lo <= hi:
        mid = (lo + hi) // 2

        if nums[mid] == target:
            res[0] = mid
            hi = mid - 1
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    lo = 0
    hi = len(nums) - 1

    # find last position
    while lo <= hi:
        mid = (lo + hi) // 2

        if nums[mid] == target:
            res[1] = mid
            lo = mid + 1
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return res


print(FindPArray(nums, target), "__n_t")
