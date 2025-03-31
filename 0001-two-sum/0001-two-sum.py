class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # n = len(nums)
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
            # print(hashmap)
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        
        return []


        