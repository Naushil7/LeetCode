class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        peri = 0
        nums.sort()

        for i in range(0, len(nums)-2):
            if nums[i] + nums[i+1] > nums[i+2]:
                peri = nums[i] + nums[i+1] + nums[i+2]
        

        return peri