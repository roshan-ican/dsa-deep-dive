# "example": "heights = [3,1,5,6,2,3] -> 10",

heights =  [2, 1, 5, 6, 2, 3]

stack = []
max_area = 0

for r in range(len(heights)):
    current = heights[r]
    while stack and current < heights[stack[-1]]:
        p_index = stack.pop()
        height = heights[p_index]
        
        if stack:
            width = r - stack[-1] - 1
        else:
            width = r
        
        area = height * width
        max_area = max(max_area, area)
        
    stack.append(r)
    

        
        
print(max_area)
print(stack)