# input:
# [10,20,30,40]
# [10,15,20,10,15,20,10,15,20,10,10,15,20,10,15,20,10,15,20,10,10,15,20,10,15,20,10,15,20,10,10,15,20,10,15,20,10,15,20,10,10,15,20,10,15,20,10,15,20,10,10,15,20,10,15,20,10,15,20,10,10,15,20,10,15,20,10,15,20,10,10,15,20,10,15,20,10,15,20,10,10,15,20,10,15,20,10,15,20,10,10,15,20,10,15,20,10,15,20,10]

## attempt II - bottom up
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [cost[0], cost[1]]
        for i in range(2,n):
            dp.append(cost[i] + min(dp[i-1], dp[i-2]))
        return min(dp[n-1], dp[n-2])

# attempt I - recurssion + memo
# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         self.memo ={}
#         a = min(self.solve(cost, 0), self.solve(cost, 1))
#         print(self.memo)
#         return a
    
#     def solve(self, cost, i):
#         if i >= len(cost):
#             return 0
#         elif i not in self.memo.keys():
#             self.memo[i] = cost[i] + min(self.solve(cost, i+1), self.solve(cost, i+2))
#         return self.memo[i]
      