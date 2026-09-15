# Longest Substring Without Repeating Characters
# Medium
# Topics
# Company Tags
# Hints
# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.


# Example 1:

# Input: s = "zxyzxyz"

# Output: 3
# Explanation: The string "xyz" is the longest without duplicate characters.


# Example 2:

# Input: s = "xxxx"

# Output: 1

# Constraints:


# 0 <= s.length <= 50,000
# s may consist of printable ASCII characters.
def longest_sub(s):
    last_see = set()
    left = 0
    longest = 0
    
    for i, n in enumerate(s):
        while n in last_see:
            last_see.remove(s[left])
        last_see.add(n)
        longest = max(longest, i - left + 1)
    return longest


print(longest_sub("zxyzxyz"))

