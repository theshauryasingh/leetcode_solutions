##input
# "abcde"
# "ace"
# "abc"
# "abc"
# "abc"
# "def"

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.memo = {}
        return self.solve(text1, text2)
        
    def solve(self, text1, text2):
        if text1 == '' or text2 == '':
            return 0
        elif (text1, text2) not in self.memo.keys():
            if text1[0] == text2[0]:
                self.memo[(text1, text2)] =  1 + self.solve(text1[1:], text2[1:])
            else:
                self.memo[(text1, text2)] = max(self.solve(text1[1:], text2), self.solve(text1, text2[1:]))
        return self.memo[(text1, text2)]

## Attempt I - recursion 
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