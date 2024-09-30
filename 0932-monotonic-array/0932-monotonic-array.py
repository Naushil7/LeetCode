class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last = 0
        cnt = 0
        start = 0
        nxt = 1 

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] and nxt < len(nums)-1:
                start += 1
                nxt += 1
            else:
                break
                
        if len(nums) == 1:
            return True

        elif nums[start] >= nums[nxt]:
            for i in range(len(nums)-1):
                if nums[i] >= nums[i+1]:
                    last = nums[i+1]
                    cnt +=1
                else:
                    return False

            if cnt == len(nums)-1:
                return True
            else:
                return False

        elif nums[start] <= nums[nxt]:
            for i in range(len(nums)-1):
                if nums[i] <= nums[i+1]:
                    last = nums[i+1]
                    cnt +=1
                else:
                    return False

            if cnt == len(nums)-1:
                return True
            else:
                return False