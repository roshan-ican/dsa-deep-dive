from collections import Counter


def firstUniqChar(s: str) -> int:
        count = {}
        for i, n in enumerate(s):
            count[n] = i

        for k, v in Counter(s).items():
        
            if v == 1:
                return count[k]
        return -1
s = "leetcode"
print(firstUniqChar(s))