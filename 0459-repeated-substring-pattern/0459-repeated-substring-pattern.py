class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in s[1:] + s[:-1]
        # dict_1 = {}
        # for i in range(len(s)):
        #     if s[i] in dict_1:
        #         dict_1[s[i]] += 1
        #     else:
        #         dict_1[s[i]] = 1
         
        # # print(dict_1)
        # first_value = dict_1.values()[0]
        # print(first_value)
        # for i in dict_1:
        #     if first_value != dict_1[i] or len(s) == 1:
        #         return False
        # sub = ''
        # dict_1 = {}
        # for i in range(len(s)-1):
        #     if s[i] != s[i+1] and s[i] not in sub:
        #         sub += s[i]
        #     elif len(s) == 1:
        #         sub = s[0]
        #     elif s.count(s[i]) == len(s):
        #         sub = s[0]

        # print(sub)    
        
        # count = s.count(sub)
        # print(count)
        
        # if (count * len(sub)) == len(s):
        #     return True
        # else:
        #     return False