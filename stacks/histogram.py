# "example": "heights = [3,1,5,6,2,3] -> 10",

heights = [2, 1, 5, 6, 2, 3]

stack = []

for r in range(len(heights)):
    current = heights[r]
    while stack and current < stack[-1]:
        stack.pop()
    stack.append(current)
    

    if heights[r] > heights[l]:
        stack.pop(heights.index(h))
    else:
        stack.pop(heights.index(s2))
        
        
print(stack)
print(stack)