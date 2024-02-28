class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # brute force - hashmap and check frequency - time:On - space:On
        # iterate over every item and XOR together  - time:On - space:O1
        # binary search
        ##inps
        # [1,1,2,3,3,4,4,8,8]
        # [3,3,7,7,10,11,11]
        # [1,3,3,7,7,11,11]
        # [3,3,7,7,11,11,12]
        # [3,3,7,7,10,11,11,12,12]
        l = 0
        r = len(nums) #not in considered list
        while(l<r-1):
            mid = l + int((r-l)/2)
            print(mid, nums[l:r])
            if nums[mid] == nums[mid+1]:
                if (r-(mid + 1)) %2 == 0 :
                    #definitely at right of mid
                    l = mid+2
                else:
                    #definitely at left of mid
                    r = mid
            else:
                if (r-(mid + 1)) %2 == 0:
                    #definitely at left of mid
                    r = mid+1
                else:
                    #definitely at right of mid
                    l = mid+1
        return nums[l]