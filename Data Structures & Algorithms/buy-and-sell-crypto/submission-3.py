class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start, end = 0, 1

        profit = 0
        while end < len(prices):
            if prices[start] <= prices[end]:
                new_profit = prices[end] - prices[start]
                if new_profit > profit:
                    profit = new_profit
                end += 1
            else:
                start = end
                end += 1
        return profit