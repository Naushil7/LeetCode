class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        final = ''
        i, j = 0, len(s) - 1 
        
        while i <= j:
            if s[i] == ' ':
                final += res[::-1]
                final += s[i] 
                res = ''
                i += 1
            else:
                res += s[i]
                i += 1
        
        final += res[::-1]
        
        
        return final