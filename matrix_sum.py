
def matrixSum(matrix):
    row_length = len(matrix)
    col_length = len(matrix[0])
    danger_columns = set()
    sum = 0
    for row in range(row_length):
        for column in range(col_length): 
            if matrix[row][column] == 0:
                danger_columns.add(column)
            if column in danger_columns:
                continue
            else:
                sum += matrix[row][column]
    return sum 


matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]

sum = matrixSum(matrix)
print(sum)