class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        res = []
        for i in range(len(haystack)):
            if len(haystack[i:(i+len(needle))]) == len(needle):
                print("first")
            #     if haystack[i] == needle[0]:
                if haystack[i:(i+len(needle))] in needle:
                    res.append(i)
                    print(res)
        
        if len(res) == 0:
            return -1
        else:
            return res[0]
