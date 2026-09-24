grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8

def countNegatives(grid):

    count = 0
    rows = len(grid)
    cols = len(grid[0])

    row = 0
    col = cols - 1

    while row < rows and col >= 0:
        currrent = grid[row][col]
        if currrent < 0:
            count += rows - row
            col -= 1
        else:
            row = row + 1
    return count
print(countNegatives(grid))
