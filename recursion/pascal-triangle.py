def getRows(numberOfRows):
    if numberOfRows == 1:
        return [[1]]

    triangle = getRows(numberOfRows - 1)
    prev_row = triangle[-1]
    new_row = [1]

    for i in range(len(prev_row) - 1):
        new_row.append(prev_row[i] + prev_row[i + 1])

    new_row.append(1)
    triangle.append(new_row)

    return triangle


print(getRows(3))