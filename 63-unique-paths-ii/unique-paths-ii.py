class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.memo = {}
        self.obstacleGrid = obstacleGrid
        return self.solve(len(obstacleGrid[0]), len(obstacleGrid))
        
    def solve(self, m, n):
        if self.obstacleGrid[n-1][m-1] == 1:
            return 0
        if m == 1 and n == 1:
            return 1
        if m == 0 or n == 0:
            return 0
        if (m-1, n) not in self.memo:
            self.memo[(m-1, n)] = self.solve(m-1, n)
        if (m, n-1) not in self.memo:
            self.memo[(m, n-1)] = self.solve(m, n-1)
        return self.memo[(m-1, n)] + self.memo[(m, n-1)]