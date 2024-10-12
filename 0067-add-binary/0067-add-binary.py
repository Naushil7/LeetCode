class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num1 = 0
        num2 = 0
        x = 0
        y = 0

        for i in range(len(a) - 1, -1, -1):
            # print("A: ", a[i], x)
            num1 += int(a[i]) * 2**x
            x += 1

        for j in range(len(b) - 1, -1, -1):
            # print("B: ", b[j], y)
            num2 += int(b[j]) * 2**y
            y += 1 

        print(num1)
        print(num2)

        num3 = (num1 + num2) 
        res = ""

        while num3 > 0:
            if num3 % 2 == 1:
                res = "1" + res
            else:
                res = "0" + res
            num3 //= 2

        return res if res != "" else "0"