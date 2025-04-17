class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        Type = 0  # 0 = not decided, 1 = decreasing, 2 = increasing
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                if Type == 0:
                    Type = 1  # set as decreasing
                elif Type == 2:
                    return False  # conflict: was increasing before
            elif nums[i] < nums[i+1]:
                if Type == 0:
                    Type = 2  # set as increasing
                elif Type == 1:
                    return False  # conflict: was decreasing before
        
        return True