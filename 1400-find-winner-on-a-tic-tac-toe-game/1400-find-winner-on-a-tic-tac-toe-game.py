class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        turn = 1
        empty = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for move in moves:
            i, j = move
            if empty[i][j] == 0 and turn%2 != 0:
                empty[i][j] = "X"
                turn += 1
            elif empty[i][j] == 0 and turn%2 == 0:
                empty[i][j] = "O"
                turn += 1

            # Row Win
            if empty[i][0] == empty[i][1] == empty[i][2] != 0:
                return "A" if empty[i][0] == "X" else "B"

            # Column win
            if empty[0][j] == empty[1][j] == empty[2][j] != 0:
                return "A" if empty[0][j] == "X" else "B"

            # Diagonal win (top-left to bottom-right)
            if i == j and empty[0][0] == empty[1][1] == empty[2][2] != 0:
                return "A" if empty[0][0] == "X" else "B"

            # Anti-diagonal win (top-right to bottom-left)
            if i + j == 2 and empty[0][2] == empty[1][1] == empty[2][0] != 0:
                return "A" if empty[0][2] == "X" else "B"

        for row in empty:
            if 0 in row:
                return "Pending"

        return "Draw"
        # cntx = 0
        # cnty = 0
        # # Diagnal Win
        # for i in range(3):
        #     i = j
        #     if empty[i][j] == "X":
        #         cntx += 1
        #         print(cntx)
        #         if cntx == 3:
        #             return "A"
        #     elif empty[i][j] == "O":
        #         cnty += 1
        #         print(cnty)
        #         if cnty == 3:
        #             return "B"
        # # Anti Diagnal Win
        # cntx = 0
        # cnty = 0
        # j = 2
        # for i in range(3):
        #     if empty[i][j] == "X":
        #         cntx += 1
        #         print(cntx)
        #         if cntx == 3:
        #             return "A"
        #     elif empty[i][j] == "O":
        #         cnty += 1
        #         print(cnty)
        #         if cnty == 3:
        #             return "B"
        #     j -= 1

        # # Row Win
        # for i in range(3):
        #     cntx = 0
        #     cnty = 0 
        #     for j in range(3):
        #         if empty[i][j] == "X":
        #             cntx += 1
        #             print(cntx)
        #             if cntx == 3:
        #                 return "A"
        #         elif empty[i][j] == "O":
        #             cnty += 1
        #             print(cnty)
        #             if cnty == 3:
        #                 return "B"
    
        # for j in range(3):  # Loop over columns
        #     cntx = 0
        #     cnty = 0
        #     for i in range(3):
        #         if empty[i][j] == "X":
        #             cntx += 1
        #             print(cntx)
        #             if cntx == 3:
        #                 return "A"
        #         elif empty[i][j] == "O":
        #             cnty += 1
        #             print(cnty)
        #             if cnty == 3:
        #                 return "B"

        # print(empty)

        # return "Draw"