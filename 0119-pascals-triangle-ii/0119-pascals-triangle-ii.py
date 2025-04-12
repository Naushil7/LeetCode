class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        # res = [1]
        
        # # if rowIndex == 0:
        # #     return res 

        # for i in range(rowIndex):
        #     next_row = [0] * (len(res)+1)
        #     for j in range(len(res)):
        #         next_row[j] += res[j]
        #         next_row[j+1] += res[j]
        #     res = next_row
            
        # return res

        def helper(i, row_i, rowIndex):
            if i == rowIndex:
                return row_i

            i += 1
            next_row = [0] * (i + 1)

            for j in range(i + 1):
                if j == 0 or j == i:
                    next_row[j] = 1
                else:
                    next_row[j] = row_i[j-1] + row_i[j]

            return helper(i, next_row, rowIndex)

        row_i = [1]
        return helper(0, row_i, rowIndex)
        
        
        
        