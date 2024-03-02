class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        dp = [1,2]
        for i in range (2,n):
            dp.append(dp[i-1] + dp[i-2])
        # print(dp)
        return dp[n-1]

# approach I
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         self.memo = {}
#         a = self.solve(n)
#         print(self.memo)
#         return a
    
#     def solve(self, n):
#         if n in self.memo.keys():
#             return self.memo[n]
#         if n == 1:
#             return 1
#         elif n == 2:
#             return 2
#         else:
#             self.memo[n] = self.solve(n-1) + self.solve(n-2)
#             return self.memo[n]