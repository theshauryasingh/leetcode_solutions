## third approach + selecting first letter + recursion + not storing encoded strings + memoization
## success @ "12"
#            "226"
#            "06"
class Solution:
    def solve(self, s):
        if len(s) == 0:
            return 1
        if s in self.memo.keys():
            return self.memo[s]
        a = 0
        b = 0
        if s[0] != '0':
            a = self.solve(s[1:])
        if len(s)>=2 and s[0] != '0' and int(s[0:2]) < 27:
            b = self.solve(s[2:])
        out = a+b
        self.memo[s] = out
        return out
    
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        elif "00" in s:
            return 0
        self.memo = {}
        return self.solve(s)

## second approach + selecting last letter + recursion + not storing encoded strings
## success @ "12"
#            "226"
#            "06"
## failed  @ "111111111111111111111111111111111111111111111"
# class Solution:
#     def solve(self, s):
#         if len(s) == 0:
#             self.count +=1
#             return
#         if s[-1] != '0':
#             self.solve(s[:-1])
#         if len(s)>=2 and s[-2] != '0' and int(s[-2:]) < 27:
#             self.solve(s[:-2])
#         return
    
#     def numDecodings(self, s: str) -> int:
#         if s[0] == "0":
#             return 0
#         elif "00" in s:
#             return 0
#         self.count = 0
#         self.solve(s)
#         return self.count


## first approach + selecting last letter + storing encoded strings(reverse)
## success @ "12"
#            "226"
#            "06"
## failed  @ "111111111111111111111111111111111111111111111"
# class Solution:
#     def solve(self, s, decodedS):
#         if len(s) == 0:
#             self.ans.append(decodedS)
#             return
#         if s[-1] != '0' and int(s[-1]) < 27:
#             self.solve(s[:-1], decodedS + chr(int(s[-1]) + 96))
#         if len(s)>=2 and s[-2] != '0' and int(s[-2:]) < 27:
#             self.solve(s[:-2], decodedS + chr(int(s[-2:]) + 96))
#         return 
    
#     def numDecodings(self, s: str) -> int:
#         if s[0] == "0":
#             return 0
#         self.ans = []
#         self.solve(s, '')
#         return len(self.ans)