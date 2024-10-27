class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = []
        column = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.append(i)
                    column.append(j) 

        # print(row, column)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row:
                    matrix[i][j] = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j in column:
                    matrix[i][j] = 0