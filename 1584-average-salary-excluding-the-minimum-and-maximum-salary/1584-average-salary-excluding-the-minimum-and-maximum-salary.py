class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        maxi = 0
        mini = salary[0]
        for i in range(len(salary)):
            if salary[i] >= maxi:
                maxi = salary[i]
            
            if salary[i] <= mini:
                mini = salary[i]
        
        salary.remove(maxi)
        salary.remove(mini)

        avg = float(sum(salary)) / len(salary)

        return avg