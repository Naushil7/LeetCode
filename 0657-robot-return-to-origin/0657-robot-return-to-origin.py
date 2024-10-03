class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        start = [0, 0]
        for i in moves:
            if i == "R":
                # start[0] = start[0] + 1
                start[1] = start[1] + 1
            elif i == "L":
                # start[0] = start[0] + 1
                start[1] = start[1] - 1
            elif i == "U":
                start[0] = start[0] + 1
                # start[1] = start[1] + 1
            elif i == "D":
                start[0] = start[0] - 1
                # start[1] = start[1] + 1
            
            # print(start)
        if start == [0,0]:
            return True