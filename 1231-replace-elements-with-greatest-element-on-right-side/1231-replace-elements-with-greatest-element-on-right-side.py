class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # for i in range(len(arr)):
        #     if i == len(arr)-1:
        #         arr[i] = -1
        #     elif i == len(arr)-2:
        #         arr[i] = arr[i+1]
        #     else:  
        #         arr[i] = max(arr[i+1:])
        
        i = len(arr) - 1
        max_val = -1     

        while i >= 0:
            current = arr[i] 
            arr[i] = max_val 
            max_val = max(max_val, current)  
            i -= 1 

        return arr
        