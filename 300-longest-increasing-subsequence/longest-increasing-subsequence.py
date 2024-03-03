class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        maxCount = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            maxCount = max(dp[i], maxCount)
        print(dp)
        return maxCount
                
        
                    
                    
                
                    