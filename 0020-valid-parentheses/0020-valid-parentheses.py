class Solution:
    def isValid(self, s: str) -> bool:

        hashmap = {
            '(':')',
            '[':']',
            '{':'}'
        }

        stack = []

        for i in s:
            if i in hashmap.keys():
                stack.append(i)
            else:
                if stack == []:
                    return False
                top = stack.pop()
                if hashmap[top] != i:
                    return False

        return not stack  
