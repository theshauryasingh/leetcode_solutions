##input
# "abcde"
# "ace"
# "abc"
# "abc"
# "abc"
# "def"
# "bsbininm"
# "jmjkbkjkv"


# Attempt III - bottom up
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        dp = [[0]*(n1+1) for i in range(n2+1)] # [[0]*(n1+1)]*(n2+1)
        for i in range(1, n2+1):
            for j in range(1, n1+1):
                if text2[i-1] == text1[j-1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        print(dp)
        return dp[n2][n1]
    
#      b  s  b  i  n  i  n  m
# [[0, 1, 1, 2, 2, 2, 2, 2, 2],
# j[0, 1, 1, 2, 2, 2, 2, 2, 2], 
# m[0, 1, 1, 2, 2, 2, 2, 2, 2], 
# j[0, 1, 1, 2, 2, 2, 2, 2, 2], 
# k[0, 1, 1, 2, 2, 2, 2, 2, 2], 
# b[0, 1, 1, 2, 2, 2, 2, 2, 2], 
# k[0, 1, 1, 2, 2, 2, 2, 2, 2], 
# j[0, 1, 1, 2, 2, 2, 2, 2, 2], 
# k[0, 1, 1, 2, 2, 2, 2, 2, 2], 
# v[0, 1, 1, 2, 2, 2, 2, 2, 2]] 
# 9 8

# 2 8
# [[0, 0, 0, 0, 0, 0, 0, 0, 1], 
#  [0, 0, 0, 0, 0, 0, 0, 0, 1], 
#  [0, 0, 0, 0, 0, 0, 0, 0, 1], 
#  [0, 0, 0, 0, 0, 0, 0, 0, 1], 
#  [0, 0, 0, 0, 0, 0, 0, 0, 1], 
#  [0, 0, 0, 0, 0, 0, 0, 0, 1], 
#  [0, 0, 0, 0, 0, 0, 0, 0, 1], 
#  [0, 0, 0, 0, 0, 0, 0, 0, 1], 
#  [0, 0, 0, 0, 0, 0, 0, 0, 1], 
#  [0, 0, 0, 0, 0, 0, 0, 0, 1]] 


# # Attempt II - recursion  - memo
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         self.memo = {}
#         return self.solve(text1, text2)
        
#     def solve(self, text1, text2):
#         if text1 == '' or text2 == '':
#             return 0
#         elif (text1, text2) not in self.memo.keys():
#             if text1[0] == text2[0]:
#                 self.memo[(text1, text2)] =  1 + self.solve(text1[1:], text2[1:])
#             else:
#                 self.memo[(text1, text2)] = max(self.solve(text1[1:], text2), self.solve(text1, text2[1:]))
#         return self.memo[(text1, text2)]

## Attempt I - recursion  - failed
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         return self.solve(text1, text2)
        
#     def solve(self, text1, text2):
#         if text1 == '' or text2 == '':
#             return 0
#         elif text1[0] == text2[0]:
#             return 1 + self.solve(text1[1:], text2[1:])
#         else:
#             return max(self.solve(text1[1:], text2), self.solve(text1, text2[1:]))