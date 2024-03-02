class Solution:
    def isHappy(self, n: int) -> bool:
        hashSet = set()
        hashSet.add(n)
        while(n!=1):
            num = 0
            while(n!=0):
                temp = n%10
                num += temp * temp
                n = int(n/10)
            if num in hashSet:
                return False
            hashSet.add(num)
            n = num
            # print(hashSet, num)
        return True
    
    # def isHappy(self, n: int) -> bool:
    #     hashSet = set()
    #     hashSet.add(n)
    #     while(n!=1):
    #         num = 0
    #         temp = n%10
    #         while(temp>1):
    #             num += temp * temp
    #             temp = int(n/10)
    #         num += temp * temp
    #         if num in hashSet:
    #             return False
    #         hashSet.add(num)
    #         n = num
    #         print(hashSet, num, temp)
    #         break
    #     return True