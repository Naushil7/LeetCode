class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap={
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        start = 0
        end = len(s) - 1
        res = 0

        while end >= start:
            if end > 0 and s[end - 1] == 'C' and s[end] == 'D' :
                res += 400
                end -= 2
            elif end > 0 and s[end - 1] == 'C' and s[end] == 'M':
                print(res, '2.1', end)
                res += 900
                end -= 2
            elif end > 0 and s[end - 1] == 'X' and s[end] == 'L':
                res += 40
                end -= 2
            elif end > 0 and s[end - 1] == 'X' and s[end] == 'C':
                res += 90
                end -= 2
            elif end > 0 and s[end - 1] == 'I' and s[end] == 'V':
                res += 4
                end -= 2
            elif end > 0 and s[end - 1] == 'I' and s[end] == 'X':
                res += 9
                end -= 2
            else:
                res += hashmap[s[end]]
                end -= 1

        return res