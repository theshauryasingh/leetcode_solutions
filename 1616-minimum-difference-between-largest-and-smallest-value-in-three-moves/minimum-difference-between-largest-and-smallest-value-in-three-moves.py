class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <=3:
            return 0
        nums.sort()
        i = 1
        mindiff = float(inf)
        while(i<=4):
            curdiff = abs(nums[n - i] - nums[4 - i])
            mindiff = min(mindiff, curdiff)
            i+=1
        return mindiff    
            
        # nums.sort()
        # difference_arr = [-1]*(len(nums)-1)
        # i = 0
        # while(i< len(nums)-1):
        #     difference_arr[i] = nums[i+1] - nums[i]
        #     i+=1
        # counter = 3
        # l = 0
        # r = len(difference_arr)-1
        # print(difference_arr, l, r, counter)
        # while(counter>0 and l<=r):
        #     if difference_arr[l]>difference_arr[r]:
        #         l+=1
        #     else:
        #         r-=1
        #     counter -=1
        # print(difference_arr, l, r, counter)
        # if r<l:
        #     return 0
        # return max(difference_arr[l],difference_arr[r])