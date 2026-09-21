# # 1. Maximum sum of a fixed-size subarray
# # Return the largest sum of any k consecutive numbers.
# # Example 1
# # Input:    numbers = [2, 1, 5, 1, 3, 2], k = 3
# # Expected: 9
# # Example 2
# # Input:    numbers = [2, 3, 4, 1, 5], k = 2
# # Expected: 7

# def largest_sum(numbers, k):
    
#     left  = 0
#     window_sum = sum(numbers[:k])
    
#     for right in range(len(numbers)):
#     curr_sum = numbers[right] - numbers[left ]+ 1
#     if curr_sum > window_sum:
#             window_sum = window_sum
#             left += 1
#         curr_sum+=numbers[right]
#         window_sum = max(window_sum, currSum)
    
#     return window_sum
    
        
        
# numbers = [2, 3, 4, 1, 5], k = 2
# print(largest_sum, numbers)