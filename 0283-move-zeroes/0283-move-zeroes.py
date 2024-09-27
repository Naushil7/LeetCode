class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        res = []
        zero = []
        # for i in range(len(nums)):
        #     # print(nums[i])
        #     if nums[i] == 0:
        #         zero.append(nums[i])
        #     else:
        #         res.append(nums[i])

        # print(res)
        # print(zero)
        for i in range(len(nums)):
            # print(nums[i])
            if nums[i] == 0:
                nums.append(nums[i])
                nums.remove(nums[i])
            # else:
            #     res.append(nums[i])
        # print(nums)
        return nums