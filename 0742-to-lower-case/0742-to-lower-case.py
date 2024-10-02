class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            if 65 <= ord(s[i]) <= 90:
                res += chr(ord(s[i])+32)
            else:
                res += s[i]

        return res
        