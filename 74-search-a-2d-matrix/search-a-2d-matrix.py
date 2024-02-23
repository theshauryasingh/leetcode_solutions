class Solution:
    def binarySearch(self, nums, target):
        l = 0
        r = len(nums) - 1
        while(l<=r):
            mid = int((l+r) / 2)
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # approach 1 - flatten and then binary search
        nums = []
        for i in matrix:
            for j in i:
                # print(j)
                nums.append(j)
        return self.binarySearch(nums, target)