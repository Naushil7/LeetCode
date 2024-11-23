class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights)
        counter = 0
        
        for i,j in zip(expected, heights):
            if i != j:
                counter += 1
                
        return counter
        