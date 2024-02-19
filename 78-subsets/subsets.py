class Solution:
    def powerset(self, nums, i, subset):
        # print(nums, i, subset, ans)
        if i >= len(nums):
            self.ans.append(subset)
            return

        # self.powerset(nums, i+1, subset, ans)
        # subset.append(nums[i])
        # self.powerset(nums, i+1, subset, ans)

        self.powerset(nums, i+1, subset)
        self.powerset(nums, i+1, subset + [nums[i]])

        # self.powerset(nums, i+1, subset + [nums[i]], ans)
        # self.powerset(nums, i+1, subset, ans)

        # subset.append(nums[i])
        # self.powerset(nums, i+1, subset, ans)
        # subset.pop(-1)
        # self.powerset(nums, i+1, subset, ans)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.powerset(nums, 0, [])
        return self.ans