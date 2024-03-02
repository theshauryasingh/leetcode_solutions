class Solution:
    def numSum(self, n):
        sum = 0
        while(n>0):
            temp = n%10
            sum += temp
            n = int(n/10)
        return sum
            
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        sum = self.numSum(n)
        x = 0
        if target - sum >= 0:
            return x
        else:
            i = 10
            while(target - sum < 0):
                temp = i - n%i
                n += temp
                print(n, temp, i)
                sum = self.numSum(n)
                i *= 10
                x += temp
            return x