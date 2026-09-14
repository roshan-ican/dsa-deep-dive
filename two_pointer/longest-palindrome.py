def longest(s):
    l = 0
    r = 0
    count = ""
    for i in range(len(s)):
        l = i
        r = i
        
        while i >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > len(count):
                count = s[l:r + 1]
            l -= 1
            r += 1
    return count



s = "babad"
print(longest(s))
