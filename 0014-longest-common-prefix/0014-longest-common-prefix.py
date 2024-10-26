class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        check = ""
        max_len = len(strs[0])
        for i in strs:
            if len(i) < max_len:
                max_len = len(i)
        
        for i in range(max_len):
            for j in strs:
                if j[i] != strs[0][i]:
                    return check  
            
            check += strs[0][i]

        return check