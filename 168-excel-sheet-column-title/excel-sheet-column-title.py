class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        output = ''
        while columnNumber > 0:
            columnNumber -= 1
            output = chr((columnNumber % 26) + ord('A')) + output
            columnNumber //= 26
        return output


    
# AttemptI - 
# class Solution:
#     def convertToTitle(self, columnNumber: int) -> str:
#         output = ''
#         if columnNumber <= 26:
#             output += chr(columnNumber+64)
#         else:
#             output += chr(int(columnNumber/26)+64) #1114111 = 4294967296
#             output += chr(int(columnNumber%26)+64)
#         return output