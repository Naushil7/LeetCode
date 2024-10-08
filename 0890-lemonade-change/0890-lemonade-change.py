class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        # cash = {}
        # for i in bills:
        #     if i in cash:
        #         cash[i] += 1
        #     else:
        #         cash[i] = 1

        # print(cash)
        count_5 = 0
        count_10 = 0
        count_20 = 0
        for i in bills:
            if i == 5:
                count_5 += 1
            elif i == 10:
                if count_5 > 0:
                    count_5 -= 1
                    count_10 += 1
                else:
                    return False
            else:
                if count_5 > 0 and count_10 > 0:
                    count_5 -= 1
                    count_10 -= 1
                    count_20 += 1
                elif count_5 >= 3:
                    count_5 -= 3
                    count_20 += 1
                else:
                    return False


        return True