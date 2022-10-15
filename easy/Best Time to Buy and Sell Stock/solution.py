# Time complexity: O(n)
# Approach: Accumulate min value from left and max value from right for all indexes and get the maximum difference.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # peaks and lows in the prices
        # keep track of minimum and change minimum price is found in the next iteration
        # calculate the max_profit then
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit


