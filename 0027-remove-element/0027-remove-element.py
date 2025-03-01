class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
#         l, r = 0, len(nums)
        
#         while l < r:
#             if nums[l] == val:
#                 del nums[l]
#                 r -= 1
#             else:
#                 l += 1
        
#         return len(nums)

        k = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
                
        return k