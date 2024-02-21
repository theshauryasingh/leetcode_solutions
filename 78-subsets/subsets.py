class Solution:
    def powerset(self, nums, i, subset):
        if i >= len(nums):
            self.ans.append(subset)
            return
        self.powerset(nums, i+1, subset)
        self.powerset(nums, i+1, subset + [nums[i]])

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.powerset(nums, 0, [])
        return self.ans