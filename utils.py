def copy_2d_array(arr):
    copy = []
    for r in range(0, len(arr)):
        row = [x for x in arr[r]]
        copy.append(row)
    return copy

def copy_2d_array_inverted(arr):
    inverted = []
    for c in range(0, len(arr[0])):
        col = []
        for r in range(0, len(arr)):
            col.append(arr[r][c])
        inverted.append(col)
    return inverted