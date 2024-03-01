# inputs
# 2
# 1
# 3
# 1
# 20
# 524286
# 20
# 524285
# 29
# 524287

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # 3 -> 0110
        if n == 1:
            return 0
        length = 2**(n-2)
        if k <= length:
            return self.kthGrammar(n-1, k)
        else:
            return 1- self.kthGrammar(n-1, k-length)


# V Attempt - recursion - pattern - complement
# class Solution:
#     def getString(self, n):
#         if n == -1:
#             return '0'
#         elif n == 0:
#             return '01'
#         string = self.getString(n-1)
#         num = int(len(string)/2)
#         # return string + string[num:] + string[:num]
#         return string + self.complement(string)
    
#     def complement(self,string):
#         comp = ''
#         for letter in string:
#             comp = comp + str(1 - int(letter))
#         return comp

#     def solve(self, n):
#         if n == 0:
#             string = '0'
#         elif n == 1:
#             string = '01'
#         else:
#             string = self.getString(n-1)
#         return string
        
#     def kthGrammar(self, n: int, k: int) -> int:
#         string = self.solve(n-1)
#         print(len(string) == 2**(n-1))
#         if k <= len(string):
#             return int(string[k-1])
#         else:
#             k = k - len(string)
#             return 1 - int(string[k-1])
        

# IV Attempt - TAIL recursion - pattern
# class Solution:
#     def getString(self, n, i, c):
#         if i == n:
#             return c
#         num = int(len(c)/2)
#         return self.getString(n, i+1, c + c[num:] + c[:num])
        
#     def kthGrammar(self, n: int, k: int) -> int:
#         if n == 1:
#             return '0'
#         # elif n == 2:
#         #     return '01'
#         string = self.getString(n, 2, '01')
#         print(len(string))
#         return int(string[k-1])

# III Attempt - recursion - pattern
# class Solution:
#     def getString(self, n):
#         if n == 0:
#             return '0'
#         elif n == 1:
#             return '01'
#         string = self.getString(n-1)
#         num = int(len(string)/2)
#         return string + string[num:] + string[:num]
        
#     def kthGrammar(self, n: int, k: int) -> int:
#         string = self.getString(n-1)
#         print(len(string))
#         return int(string[k-1])

# II Attempt -recursion
# class Solution:
#     def getString(self, n):
#         if n == 1:
#             return '0'
#         string = self.getString(n-1)
#         temp = ''
#         for letter in string:
#             if letter == '0':
#                 temp += '01'
#             elif letter == '1':
#                 temp += '10'        
#         return temp
        
#     def kthGrammar(self, n: int, k: int) -> int:
#         string = self.getString(n)
#         print(string)
#         return int(string[k-1])

# I attempt
# class Solution:
#     def kthGrammar(self, n: int, k: int) -> int:
#         string = '0'
#         for i in range(1,n):
#             temp = ''
#             for letter in string:
#                 if letter == '0':
#                     temp += '01'
#                 elif letter == '1':
#                     temp += '10'
#             string = temp
#         print(string)
#         return int(string[k-1])