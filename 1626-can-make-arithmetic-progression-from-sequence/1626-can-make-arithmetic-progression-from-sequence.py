class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        cnt = 0
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(len(arr)-1):
            # print(arr[i])
            # print(arr[i+1])
            if diff == arr[i+1] - arr[i]:
                cnt += 1
                if cnt == len(arr) - 1:
                    return True
            else:
                return False