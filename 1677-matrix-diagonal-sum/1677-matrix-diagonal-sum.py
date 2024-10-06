class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        lst = []

        # For Even Matrix
        if len(mat)%2 == 0:
            # print("no overlap")
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if i == j:  
                        # print(mat[i][j])
                        lst.append(mat[i][j])
                    elif i + j == len(mat) - 1:
                        # print(mat[i][j])
                        lst.append(mat[i][j])             
            # print(sum(lst))
            return sum(lst)

        # For Square matrix with single value
        elif len(mat) == 1:
            # print(mat[0][0])
            return mat[0][0]

        else:
            print("Overlap")
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if i == j:  
                        # print(mat[i][j])
                        lst.append(mat[i][j])
                    elif i + j == len(mat) - 1:
                        # print(mat[i][j])
                        lst.append(mat[i][j])             
            # print(sum(lst))
            return sum(lst)           

        return 1