class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = {}
        a = self.solve(n)
        print(self.memo)
        return a
    
    def solve(self, n):
        if n in self.memo.keys():
            return self.memo[n]
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            self.memo[n] = self.solve(n-1) + self.solve(n-2)
            return self.memo[n]