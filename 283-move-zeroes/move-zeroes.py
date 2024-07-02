class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        ind  = 0
        temp = 0
        while(ind<n):
            if nums[ind] != 0:
                nums[temp] = nums[ind]
                temp += 1
            ind += 1
        for i in range(temp, n):
            nums[i] = 0
        return nums


# can move a single zero
# class Solution:
#     def swap(self, a, b, nums):
#         temp = nums[a]
#         nums[a] = nums[b]
#         nums[b] = temp
#         return nums
    
#     def moveZeroes(self, nums: List[int]) -> None:
#         n = len(nums)
#         ind  = 0
#         while(ind<n):
#             if nums[ind] == 0 and ind+1 < n:
#                 nums = self.swap(ind, ind+1, nums)
#             ind += 1
#         return nums
    