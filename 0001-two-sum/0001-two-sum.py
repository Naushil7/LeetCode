class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Wrong Index as sorting happens
        # result = 0
        # result_val = []

        # start = 0
        # end = len(nums) - 1

        # nums.sort()

        # while start <= end:
        #     result = nums[start] + nums[end]
        #     if result == target:
        #         result_val.append(start)
        #         result_val.append(end)                
        #         return result_val
        #     elif result > target:
        #         end -= 1
        #     else:
        #         start += 1

        # return []

        hashmap = {}

        for val in range(len(nums)):
            hashmap[nums[val]] = val

        print(hashmap)

        for val in range(len(nums)):
            remainder = target - nums[val]
            if remainder in hashmap and hashmap[remainder] != val:
                return [val, hashmap[remainder]]


        return []

