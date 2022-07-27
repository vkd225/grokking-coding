# // Transpose the matrix and return it. The matrix will be m x n where m,n >= 1 and m may not equal n.

# function transpose(matrix) {
#   return matrix;
# }

# //console.log(transpose([[1,2,3],[4,5,6],[7,8,9]]))
# // [[1,4,7],[2,5,8],[3,6,9]]

# // Walk the matrix from the upper left hand corner clockwise and outside-in. The matrix will be m x n where m,n >= 1 and m may not equal n.
# function walkSpiral(matrix) {
#   return []
# }

# // console.log(walkSpiral([[1,2,3], [8,9,4], [7,6,5]]));
# // [1,2,3,4,5,6,7,8,9]

def transpose(matrix):
    # result = matrix[:][:]
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[0])):
    #         # result[i] = [None] * len(matrix)
    #         result[i][j] = matrix[j][i]

    # return result

    if not matrix:
        return []
    return [ [ row[ i ] for row in matrix ] for i in range( len( matrix[ 0 ]))]


matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1,2],[4,5],[7,8]]
matrix3 = [[1,2,3],[4,5,6]]
matrix3 = [[1,2,3]]
matrix3 = [[1],[4],[6]]
matrix3 = [[1,2],[4,5]]
matrix3 = [[1,2,3,0],[4,5,6,10],[7,8,9,11], [12, 13, 14, 15]]
matrix4 = [[1]]
# print (transpose(matrix3))

def walkSpiral(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
            if matrix:
                result += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))

    return result


# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[1,2,3], [8,9,4], [7,6,5]]
# matrix = [[1,2],[4,5],[7,8]]
# matrix = []

matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1,2],[4,5],[7,8]]
# matrix3 = [[1,2,3],[4,5,6]]
matrix3 = [[1,2,3]]
# matrix3 = [[1],[4],[6]]
# matrix3 = [[1,2],[4,5]]
# matrix3 = [[1,2,3,0],[4,5,6,10],[7,8,9,11], [12, 13, 14, 15]]
matrix4 = [[1]]

print (walkSpiral(matrix4))


