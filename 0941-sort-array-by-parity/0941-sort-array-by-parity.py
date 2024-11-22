class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # i = len(nums) - 1
        # j = 0
        
        # while i >= j:
        #     if nums[i] % 2 == 0:
        #         swap = nums[j]
        #         nums[j] = nums[i]
        #         nums[i] = swap
        #         # print(swap, nums[i], nums[j])
        #         j += 1
                
        #     i -= 1
        j = 0 
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1

        return nums