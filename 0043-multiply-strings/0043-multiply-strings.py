class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        a = 0
        b = 0
        for i in num1:
            a = a * 10 + (ord(i) - 48)
        for i in num2:
            b = b * 10 + (ord(i) - 48) 
        
        return str(a*b)
            