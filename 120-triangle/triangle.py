## input
# [[2],[4,3],[1,2,3],[4,3,2,1]]
# [[2],[3,4],[6,5,7],[4,1,8,3]]
# [[-10]]

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        row = [0]*(len(triangle[-1])+1)
        self.dp = [row]*(len(triangle))
        self.dp[-1] = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                self.dp[i][j] = triangle[i][j] + min(self.dp[i+1][j], self.dp[i+1][j+1])
        print(self.dp)
        return self.dp[0][0]

## Attemp II - recursion + memo
# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         if len(triangle) == 1:
#             return triangle[0][0]
#         self.memo = {}
#         return triangle[0][0] + min(self.solve(triangle, 0, 1), self.solve(triangle, 1, 1))
    
#     def solve(self, triangle, i, r):
#         # print(i, r)
#         if len(triangle)-1 == r:
#             return triangle[r][i]
#         if (i, r+1) not in self.memo.keys():
#             self.memo[(i, r+1)] = self.solve(triangle, i, r+1)
#         if (i+1, r+1) not in self.memo.keys():
#             self.memo[(i+1, r+1)] = self.solve(triangle, i+1, r+1)
#         return triangle[r][i] + min(self.memo[(i+1, r+1)], self.memo[(i, r+1)])

#  I attempt
# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         sum = triangle[0][0]
#         ind = 0
#         for i in triangle[1:]:
#             if i[ind] <= i[ind + 1]:
#                 sum += i[ind]
#             else:
#                 sum += i[ind+1]
#                 ind = ind + 1
#         return sum