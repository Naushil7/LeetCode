class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        start = [0, 0]
        direction = 1
        for i in instructions:

            if i == "G" and direction == 1:
                start[1] += 1
            elif i == "G" and direction == 2:
                start[0] += 1
            elif i == "G" and direction == 3:
                start[1] -= 1 
            elif i == "G" and direction == 4:
                start[0] -= 1
            
            elif i == "L" and direction != 4:
                direction += 1
            elif i == "L" and direction == 4:
                direction = 1

            elif i == "R" and direction != 1:
                direction -= 1
            elif i == "R" and direction == 1:
                direction = 4

            print(direction)
            print(start)

        if start == [0,0] or direction != 1:
            return True