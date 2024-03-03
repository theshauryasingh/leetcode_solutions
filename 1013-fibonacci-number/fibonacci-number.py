##attempt 3 - bottom up + pointers
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        a = 0
        b = 1
        for i in range(2,n+1):
            temp = a + b
            a = b
            b = temp
        return b

##attempt 2 - bottom up + tabulation
# class Solution:
#     def fib(self, n: int) -> int:
#         self.dp = [0,1]
#         for i in range(2,n+1):
#             self.dp.append(self.dp[i-1] + self.dp[i-2])
#         return self.dp[n]
    
# attempt 1 - reccursion + memo
# class Solution:
#     def fib(self, n: int) -> int:
#         self.memo = {0:0, 1:1}
#         return self.solve(n)
    
#     def solve(self, n):
#         if n not in self.memo.keys():
#             self.memo[n] = self.solve(n-1) + self.solve(n-2)
#         return self.memo[n]