"""Run this file to see sliding-window practice prompts. Write solutions separately."""


QUESTIONS = [
    {
        "title": "1. Maximum sum of a fixed-size subarray",
        "prompt": "Return the largest sum of any k consecutive numbers.",
        "examples": [
            ("numbers = [2, 1, 5, 1, 3, 2], k = 3", "9"),
            ("numbers = [2, 3, 4, 1, 5], k = 2", "7"),
        ],
        "difficulty": "Easy",
    },
    {
        "title": "2. Contains permutation",
        "prompt": "Return True if s2 contains a permutation of s1.",
        "examples": [
            ('s1 = "ab", s2 = "eidbaooo"', "True"),
            ('s1 = "ab", s2 = "eidboaoo"', "False"),
        ],
        "difficulty": "Medium",
        "url": "https://leetcode.com/problems/permutation-in-string/",
    },
    {
        "title": "3. Find all anagrams",
        "prompt": "Return every starting index in s where an anagram of p begins.",
        "examples": [
            ('s = "cbaebabacd", p = "abc"', "[0, 6]"),
            ('s = "abab", p = "ab"', "[0, 1, 2]"),
        ],
        "difficulty": "Medium",
        "url": "https://leetcode.com/problems/find-all-anagrams-in-a-string/",
    },
    {
        "title": "4. Longest substring without repeating characters",
        "prompt": "Return the length of the longest substring with no repeated character.",
        "examples": [
            ('s = "zxyzxyz"', "3"),
            ('s = "bbbbb"', "1"),
        ],
        "difficulty": "Medium",
        "url": "https://leetcode.com/problems/longest-substring-without-repeating-characters/",
    },
    {
        "title": "5. Minimum consecutive cards",
        "prompt": "Return the smallest consecutive group containing a duplicate card, or -1.",
        "examples": [
            ("cards = [3, 4, 2, 3, 4, 7]", "4"),
            ("cards = [1, 0, 5, 3]", "-1"),
        ],
        "difficulty": "Medium",
        "url": "https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/",
    },
    {
        "title": "6. Minimum Size Subarray Sum",
        "prompt": "Return the minimum length of a contiguous subarray whose sum is at least target, or 0.",
        "examples": [("target = 7, nums = [2,3,1,2,4,3]", "2")],
        "difficulty": "Medium",
        "url": "https://leetcode.com/problems/minimum-size-subarray-sum/",
    },
    {
        "title": "7. Max Consecutive Ones III",
        "prompt": "Return the longest contiguous run of ones obtainable by changing at most k zeroes.",
        "examples": [("nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2", "6")],
        "difficulty": "Medium",
        "url": "https://leetcode.com/problems/max-consecutive-ones-iii/",
    },
    {
        "title": "8. Fruit Into Baskets",
        "prompt": "Return the longest contiguous section containing at most two distinct fruit types.",
        "examples": [("fruits = [1,2,1]", "3")],
        "difficulty": "Medium",
        "url": "https://leetcode.com/problems/fruit-into-baskets/",
    },
    {
        "title": "9. Minimum Window Substring",
        "prompt": "Return the shortest substring of s containing every character required by t.",
        "examples": [("s = 'ADOBECODEBANC', t = 'ABC'", "'BANC'")],
        "difficulty": "Hard",
        "url": "https://leetcode.com/problems/minimum-window-substring/",
    },
    {
        "title": "10. Sliding Window Maximum",
        "prompt": "Return the maximum value in every contiguous window of size k.",
        "examples": [("nums = [1,3,-1,-3,5,3,6,7], k = 3", "[3,3,5,5,6,7]")],
        "difficulty": "Hard",
        "url": "https://leetcode.com/problems/sliding-window-maximum/",
    },
]


def show_questions():
    for question in QUESTIONS:
        print(question["title"])
        print(f"Difficulty: {question['difficulty']}")
        print(question["prompt"])
        for number, (example, expected) in enumerate(question["examples"], start=1):
            print(f"Example {number}")
            print(f"Input:    {example}")
            print(f"Expected: {expected}")
        if question.get("url"):
            print(f"Problem:  {question['url']}")
        print()


if __name__ == "__main__":
    show_questions()
