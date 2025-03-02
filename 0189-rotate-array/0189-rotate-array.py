class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Trial 1: TC: O(kn) and SC: O(1)
        temp, r = 0, len(nums)-1

        while k > 0:
            temp = nums.pop(r)
            nums.insert(0, temp) # O(n)
            k -= 1
            
        
            
        