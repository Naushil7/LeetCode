class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        next_pointer = 1
        end = len(prices)
        max_profit = 0

        while next_pointer < end:
            if prices[start] > prices[next_pointer]:
                # print(start, next_pointer, max_profit, 'before if')
                start = next_pointer
                # print(start, next_pointer, max_profit, 'After if')
            else:
                max_profit = max(max_profit, prices[next_pointer] - prices[start])
                next_pointer += 1
                # print(start, next_pointer, max_profit, 'After else')

        return max_profit