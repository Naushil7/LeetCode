class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # res = []
        # for i in range(len(digits)):
    
        #     if i == len(digits)-1:
        #         digits[i] += 1
        #         if digits[i] > 9:
        #             rem = digits[i] % 10
        #             car = digits[i] // 10
        #             res.append(car)
        #             res.append(rem)
        #             # print(rem)
        #             # print(car)
        #         else:
        #             res.append(digits[i])
        #     else:
        #         res.append(digits[i])
            
            # print(digits[i])
        res = ''

        for i in range(len(digits)):
            res += str(digits[i])
            if i == len(digits) - 1:
                res = str(int(res)+ 1)

        res_lst = [int(char) for char in res]

        print(res)
        print(res_lst)

        return res_lst