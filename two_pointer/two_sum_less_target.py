# 3630 · Two Sum Less Than Target
# Algorithms
# Easy
# Accepted Rate
# 36%

# Description
# Solution25
# Notes
# Discuss3
# Leaderboard
# Record

# Description
# Given an array of integers nums and an integer target, if there exists i < j such that nums[i] + nums[j] < target, then return the maximum and that satisfy this condition. If no i, j satisfying the above condition exists, then -1 is returned.

# LintCode - Online Judge Solution

# Candidate Written Test Screening, Team Competency Assessment, Programming Teaching Exercises, Online Exam Grading

# WeChat for information


# 1
# ≤
# n
# u
# m
# s
# .
# l
# e
# n
# g
# t
# h
# ≤
# 1000
# 1≤nums.length≤1000
# −
# 1000
# ≤
# n
# u
# m
# s
# [
# i
# ]
# ≤
# 1000
# −1000≤nums[i]≤1000
# −
# 2000
# ≤
# t
# a
# r
# g
# e
# t
# ≤
# 2000
# −2000≤target≤2000

# Example
# Example 1:

# Input:
# nums = [2, 7, 11, 15], target = 24
# Output:
# 22
# Explanation:
# 7 + 15 = 22 < 24
# 11 + 15 = 26 > 24
# 22 is the maximum sum that satisfies the condition
# Example 2:

# Input:
# nums = [3, 5, 1, 9, 7], target = 3
# Output:
# -1
# Explanation:
# Cannot find two elements whose sum is less than 3
# Tags
# Recommend Courses

# ACM金牌逐行带刷班
# 最适合懒人的刷题课--躺平看算法大神在线coding，讲解思路+现场debug，手撕面试高频题
from typing import (
    List,
)

class Solution:
    """
    @param nums: An array of integer
    @param target: An inte  ger
    @return: The sum of two numbers smaller than target
    """
    def two_sum_less_than_target(self, nums: List[int], target: int) -> int:
        # write your code here
        nums.sort()
        left = 0
        right = len(nums) - 1
        ans = float("-inf")
        while left < right:
            sumNear = nums[left] + nums[right]
     
            if sumNear < target:
                ans = max(ans, sumNear)
                left+=1
            else:
                right -= 1

        if ans == float("-inf"):
            return -1
        return ans

sol = Solution()
nums, target = [2, 7, 11, 15], 24
print(sol.two_sum_less_than_target(nums, target))