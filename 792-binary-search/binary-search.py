class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1
        while(l<=r):
            mid = int((l+r)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
    
        ## failed approach
        # print(nums)
        # if len(nums) == 1:
        #     if target == nums[0]:
        #         return 0
        #     else:
        #         return -1
        # n   = len(nums)
        # mid = int(n/2)
        # val = nums[mid]
        # if val == target:
        #     return mid
        # elif val < target:
        #     return mid + 1 + self.search(nums[mid+1:n], target)
        # return self.search(nums[0:mid], target)