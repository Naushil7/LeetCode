class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = [word for word in s.split(' ') if word != '']

        return len(res[-1])