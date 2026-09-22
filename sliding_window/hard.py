def hard(s1, s2):
    start = s2[0]
    end = s2[-1]
    print(start, end)
    res = ""
    left = 0
    n = len(s1)
    for right in range(n):
        if s1[right] == start and s1[right] == end:
            res+=s1[left]
            left+=1
    print(res)
            



s1, s2 = "OUZODYXAZV", "XYZ"
print(hard(s1, s2))