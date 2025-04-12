class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # n = len(nums)
        # nums.sort()
        # result = set()
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         for k in range(j + 1, n):
        #             # print(nums[i], nums[j], nums[k])
        #             res = 0
        #             res = nums[i] + nums[j] + nums[k]
        #             if res == 0:
        #                 temp = []
        #                 temp.append(nums[i])
        #                 temp.append(nums[j])
        #                 temp.append(nums[k])
        #                 if tuple(temp) not in result:
        #                     result.add(tuple(temp))
        # return list(result)

        n = len(nums)
        nums.sort()
        result = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # skip duplicate i
            
            j, k = i + 1, n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # skip duplicate j
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    # skip duplicate k
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1

                elif total < 0:
                    j += 1
                else:
                    k -= 1

        return result