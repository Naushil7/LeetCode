class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        count_0 = 0
        for i in arr:
            if i == 0:
                count_0 += 1
            
        i = len(arr) - 1
        j = len(arr) - 1 + count_0
        
        while i != j:
            if j < len(arr):
                arr[j] = arr[i]
            j -= 1
            
            if arr[i] == 0:
                if j < len(arr):
                    arr[j] = arr[i]
                j -= 1
            i -= 1
                
            
            
        