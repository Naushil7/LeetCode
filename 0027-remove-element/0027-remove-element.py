class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # for i in nums:
        #     if val in nums:
        #         nums.remove(val)

        while val in nums:
            nums.remove(val) 