class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        range_set = [] 
        
        for i in range(len(nums)):
            range_set.append(i+1)
        
        range_set = set(range_set)
        
        nums = set(nums)
        
        diff_set = range_set - nums
        
        diff_set = list(diff_set)
        
        return diff_set