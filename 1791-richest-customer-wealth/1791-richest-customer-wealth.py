class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        lst = []
        for account in accounts:
            lst.append(sum(account))
        
        return max(lst)