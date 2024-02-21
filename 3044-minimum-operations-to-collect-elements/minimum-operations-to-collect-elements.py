class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:     
        # approach 1
        n = len(nums)
        if k == n:
            return k
        counter = 0
        i = n-1
        coll = [False]*k
        while(i > -1):
            # print(i, nums[i], coll)
            if nums[i] <= k:
                coll[nums[i]-1] = True
            if False not in coll:
                break
            counter +=1
            i -=1
        return counter+1