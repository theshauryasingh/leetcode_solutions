class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        newNums = [0]*int(n/2)
        i=0
        while(i<len(newNums)):
            a = i & 1
            if a == 0:
                newNums[i] = min(nums[2 * i], nums[2 * i + 1])
            else:
                newNums[i] = max(nums[2 * i], nums[2 * i + 1])
            i+=1
        print(newNums)
        return self.minMaxGame(newNums)
                
        