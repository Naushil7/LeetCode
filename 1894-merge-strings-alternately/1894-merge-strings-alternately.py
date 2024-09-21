class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        final = ''
        for i in range(len(word1)):
            # print(len(word1))
            final += word1[i]
            if len(word1) < len(word2):
                if len(word1) - 1 != i:
                    final += word2[i]
                else:
                    final += word2[i:]
            elif len(word1) > len(word2):
                if (len(word2) - 1) >= i:
                    final += word2[i]
                else:
                    final += word1[i+1:]
                    if len(final) == len(word1) + len(word2):
                        break
            else:
                final += word2[i]

        # print(final)
        return final