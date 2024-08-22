class Solution:
    def romanToInt(self, s: str) -> int:
        s = s.upper()
        st = len(s)
        roman = 0

        for i in range (st):
            if i > 0:
                if s[i] == "I":
                    roman += 1

                elif s[i] == "V":
                    if s[i-1] == "I":
                        roman += 3
                    else:
                        roman += 5

                elif s[i] == "X":
                    if s[i-1] == "I":
                        roman += 8
                    else:
                        roman += 10

                elif s[i] == "L":
                    if s[i-1] == "X":
                        roman += 30
                    else:
                        roman += 50

                elif s[i] == "C":
                    if s[i-1] == "X":
                        roman += 80
                    else:
                        roman += 100 

                elif s[i] == "D":
                    if s[i-1] == "C":
                        roman += 300
                    else:
                        roman += 500

                elif s[i] == "M":
                    if s[i-1] == "C":
                        roman += 800
                    else:
                        roman += 1000
            else:
                if s[i] == "I":
                    roman += 1

                elif s[i] == "V":
                    roman += 5

                elif s[i] == "X":
                    roman += 10

                elif s[i] == "L":
                    roman += 50

                elif s[i] == "C":
                    roman += 100 

                elif s[i] == "D":
                    roman += 500

                elif s[i] == "M":
                    roman += 1000
        return roman