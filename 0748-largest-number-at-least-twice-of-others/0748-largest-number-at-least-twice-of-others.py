class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        max_num_pl = 0
        
        for i in range(len(nums)):

            if nums[i] == max_num:
                # print(nums[i], "if", max_num, i)
                max_num_pl = i
                
            elif nums[i]*2 > max_num:
                # print(nums[i], "elif", max_num)
                return -1
            
        return max_num_pl