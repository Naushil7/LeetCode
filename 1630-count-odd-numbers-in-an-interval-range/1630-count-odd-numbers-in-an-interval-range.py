class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        # cnt = 0
        # for i in range(low, high+1):
        #     if i%2 == 0:
        #         continue
        #     else:
        #         cnt += 1
        if low % 2 == 0:
            low = low + 1
        
        if high % 2 == 0:
            high = high - 1

        if low == high:
            return 1

        odd = ((high - low)/2) + 1


        return odd