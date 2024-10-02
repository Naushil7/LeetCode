class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        score = []
        for i in range(len(operations)):
            if operations[i].lstrip('-').isdigit():
                score.append(int(operations[i]))
            elif operations[i] == "C":
                score.pop(-1)
            elif operations[i] == "D":
                score.append(int(score[-1])*2)
            elif operations[i] == "+":
                score.append(score[-1]+score[-2])

            # print(score)
        final = 0
        for i in range(len(score)):
            final += score[i]

        return final

        