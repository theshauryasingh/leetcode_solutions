class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxProfit = 0
        for i, val1 in enumerate(prices[1:]):
            if val1 < buy:
                buy = val1
            else:
                profit = val1-buy
                if profit > maxProfit:
                    maxProfit = profit
        return maxProfit

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         maxProfit = 0
#         for i, val1 in enumerate(prices[:-1]):
#             for j, val2 in enumerate(prices[i+1:]):
#                 profit = val2-val1
#                 if profit > maxProfit:
#                     maxProfit = profit
#         return maxProfit