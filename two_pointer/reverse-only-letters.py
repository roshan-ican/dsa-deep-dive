# 1725 · Reverse Only Letters
# Algorithms
# Easy
# Accepted Rate
# 71%

# Description
# Solution9
# Notes
# Discuss5
# Leaderboard
# Record
# Description
# Given a string S, return the "inverted" string. Characters that are not Latin letters remain in their original positions,
# while the positions of all Latin letters are reversed. For example, abc|jkl** is turned to lkj|cba**.

# LintCode - Online Judge Solution

# Candidate Written Test Screening, Team Competency Assessment, Programming Teaching Exercises, Online Exam Grading

# WeChat for information


# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122
# S doesn't contain \ or "
# Example
# Example 1:

# Input："ab-cd"
# Output："dc-ba"
# Explanation：The '-' stays in customary position and other characters reverse.
# Example 2:

# Input："Test1ng-Leet=code-Q!"
# Output："Qedo1ct-eeLg=ntse-T!"
# Explanation：The '-' ,'=','1', and '!'  stay in customary position and other characters reverse.
# Tags
# Company
# Microsoft
# Recommend Courses
<<<<<<< Updated upstream
def reverse(s):
    res = ""
    
    left = 0
    right = len(s)
    
    while left < right:
        if s[left].isalnum():
            left, right = right, left
=======
def reverseOnlyLetters(S):
    left = 0
    right = len(S) - 1
    S = list(S)
    while left < right:
        while left < right and not S[left].isalnum():
            left += 1
        while left < right and not S[right].isalnum():
            right -= 1
        S[left], S[right] = S[right], S[left]
        left += 1
        right -= 1
    return "".join(S)

print(reverseOnlyLetters("Test1ng-Leet=code-Q!"))
>>>>>>> Stashed changes
