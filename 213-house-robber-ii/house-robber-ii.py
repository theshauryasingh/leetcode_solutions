# input
# [1,2,3,1]
# [2,7,9,3,1,2,7,9,3,1,2,7,9,3,1,2,7,9,3,1,2,7,9,3,1,2,7,9,3,1,2,7,9,3,1,2,7,9,3,1,2,7,9,3,1,2,7,9,3,1,2,7,9,3,1,2,7,9,3,1,2,7,9,3,1,2,7,9,3,1]

# # attempt IV : dp array bottom up + variables
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        a = 0
        b = nums[0]
        for i in range(2,n):
            temp = max(b, a + nums[i-1])
            a = b
            b = temp
        one = b
        a = 0
        b = nums[1]
        for i in range(2,n):
            temp = max(b, a + nums[i])
            a = b
            b = temp
        two = b
        return max(one, two)

# # attempt III : dp array bottom up
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 1:
#             return nums[0]
#         dp = [0, nums[0]]
#         for i in range(2,n):
#             dp.append(max(dp[i-1], dp[i-2] + nums[i-1]))
#         print(dp)
#         a = max(dp[n-1], dp[n-2])
#         dp = [0, nums[1]]
#         for i in range(2,n):
#             dp.append(max(dp[i-1], dp[i-2] + nums[i]))
#         print(dp)
#         b = max(dp[n-1], dp[n-2])
#         return max(a,b)


# # attempt II : recurrsion + memo 
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]
#         self.memo = {}
#         a = self.solve(nums[:-1], 0)
#         self.memo = {}
#         b = self.solve(nums, 1)
#         return max(a, b)
    
#     def solve(self, nums, i):
#         if i >= len(nums):
#             return 0
#         if i not in self.memo.keys():
#             self.memo[i] = max(nums[i] + self.solve(nums, i+2), self.solve(nums, i+1))
#         return self.memo[i]

# attempt I : failed - recurrsion + memo 
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         self.memo = {}
#         return max(self.solve(nums,0), self.solve(nums,1))
    
#     def solve(self, nums, i):
#         if i >= len(nums):
#             return 0
#         if i not in self.memo.keys():
#             self.memo[i] = nums[i] + self.solve(nums, i+2)
#         return self.memo[i]