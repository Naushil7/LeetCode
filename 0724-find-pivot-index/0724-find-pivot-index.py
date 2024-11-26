class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            rightsum = total - nums[i] - left_sum
            if left_sum == rightsum:
                return i
            left_sum += nums[i]
            
        return -1
            
            