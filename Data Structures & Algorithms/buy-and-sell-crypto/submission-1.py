class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0
        while right < len(prices):
            temp = prices[right] - prices[left]
            profit = max(temp, profit)
            if temp < 0:
                left = right
            right = right+1
        return profit