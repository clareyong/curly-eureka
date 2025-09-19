matrix = [
    [1,2,3,14,5],
    [21,3,4,5,16],
    [3,4,15,6,7],
    [6,7,8,14,2]
]
# 68
ans = [
    [1,3,5,0,0],
    [22,25,0,0,0],
    [23,48,0,0,0],
    [0,0,0,0,0]
]

from pprint import pprint
def traverse(matrix):
    """
    given a matrix with values, find the best path to traverse to get the maximum value

    when you are at the first r and c, max you can get is 1
    when you get to [0][1], max you can get is [0][1] + [0][0]
    when you get to [1][0], max is [1][0] + [0][0]
    [1][1], max is max([1][0], [0,1]) + [1][1]
    [0][2], max is [0][1] + [0][2]
    [2][1], max is max([1][1], [2][0]) + [2][1]

    """

    nrows, ncols = len(matrix), len(matrix[0])

    result = [[0] * ncols for _ in range(nrows)]
    result[0][0] = matrix[0][0]

    for r in range(0,nrows):
        for c in range(0,ncols):
            if r-1 >= 0 and c-1 >= 0:
                result[r][c] = max(result[r-1][c], result[r][c-1]) + matrix[r][c]
            if r-1 < 0 and c-1 >= 0:
                result[r][c] = result[r][c-1] + matrix[r][c]
            if r-1 >= 0 and c-1 < 0:
                result[r][c] = result[r-1][c] + matrix[r][c]

    for row in result:
        print(row)
    return result[nrows-1][ncols-1]



print(traverse(matrix))