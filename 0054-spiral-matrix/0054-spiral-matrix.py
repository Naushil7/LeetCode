class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        lst = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        
        while left < right and top < bottom:
            for i in range(left, right):
                lst.append(matrix[top][i])
            top += 1
            
            for i in range(top, bottom):
                lst.append(matrix[i][right-1])
            right -= 1
                        
            if not (left < right and top < bottom):
                break
        
            for i in range(right - 1 , left - 1, -1):
                lst.append(matrix[bottom-1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                lst.append(matrix[i][left])
            left += 1
                

        
        # print(lst)

        return lst