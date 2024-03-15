class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # self.answer = 0
        self.memo = {}
        return self.solve(m,n)
        # return self.answer
    
    def solve(self, m, n):
        if m == 1 and n == 1 :
            # self.answer += 1
            return 1
        elif m == 0 or n == 0:
            return 0
        if (m-1, n) not in self.memo:
            self.memo[(m-1, n)] = self.solve(m-1, n)
        if (m, n-1) not in self.memo:
            self.memo[(m, n-1)] = self.solve(m, n-1)
        return self.memo[(m-1, n)] + self.memo[(m, n-1)]
        