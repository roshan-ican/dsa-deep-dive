"""Binary Search Fundamentals - Simple Explanations and Templates"""

# WHAT IS BINARY SEARCH?
# Binary search is a fast way to find something in a SORTED list.
# Instead of checking every element (slow), you eliminate half the list at each step.
# Time Complexity: O(log n) - much faster than O(n)!

# BASIC TEMPLATE
def binary_search(nums, target):
    """
    Find target in sorted array. Return index or -1 if not found.

    How it works:
    1. Start with left = 0, right = last index
    2. Find mid = (left + right) // 2
    3. If nums[mid] == target, found it!
    4. If nums[mid] < target, search right half (left = mid + 1)
    5. If nums[mid] > target, search left half (right = mid - 1)
    6. Repeat until left > right
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1  # Target is in right half
        else:
            right = mid - 1  # Target is in left half

    return -1  # Not found


# EXAMPLE: Search for 7 in [1, 3, 5, 7, 9, 11]
# Step 1: mid = 2, nums[2] = 5, too small -> left = 3
# Step 2: mid = 4, nums[4] = 9, too big -> right = 3
# Step 3: mid = 3, nums[3] = 7, found! -> return 3


# VARIANT 1: FIND LEFTMOST (First occurrence)
def binary_search_left(nums, target):
    """Find the leftmost (first) position of target"""
    left, right = 0, len(nums) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid  # Found, but keep searching left
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


# VARIANT 2: FIND RIGHTMOST (Last occurrence)
def binary_search_right(nums, target):
    """Find the rightmost (last) position of target"""
    left, right = 0, len(nums) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid  # Found, but keep searching right
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


# VARIANT 3: FIND INSERTION POSITION (Where to insert to keep sorted)
def search_insert_position(nums, target):
    """Find the position where target should be inserted"""
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid  # Already exists
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left  # Position where target should be inserted


# WHEN TO USE BINARY SEARCH:
# ✓ Array is SORTED
# ✓ Need to find something efficiently
# ✓ Time limit requires O(log n) or better

# WHEN NOT TO USE:
# ✗ Array is not sorted
# ✗ Need to find all occurrences (usually)
# ✗ Simple linear search is fast enough for small arrays


if __name__ == "__main__":
    # Test examples
    nums = [1, 3, 5, 7, 9, 11]
    print(binary_search(nums, 7))  # 3
    print(binary_search(nums, 4))  # -1

    nums_dup = [1, 3, 3, 3, 5, 7, 9]
    print(binary_search_left(nums_dup, 3))   # 1 (first 3)
    print(binary_search_right(nums_dup, 3))  # 3 (last 3)

    print(search_insert_position(nums, 6))   # 3 (insert at index 3)
