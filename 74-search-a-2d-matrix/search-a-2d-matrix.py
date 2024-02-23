class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        l = [0,0]
        r = [row - 1, col - 1]
        while(l[0]*col + l[1] <= r[0]*col + r[1]):
            sol = int((l[0]*col + l[1] + r[0]*col + r[1])/2)
            mid = [int(sol/col), sol%col]
            if matrix[mid[0]][mid[1]] == target:
                return True
            elif matrix[mid[0]][mid[1]] < target:
                if mid[1] < col - 1:
                    l = [mid[0], mid[1] + 1]
                else:
                    l = [mid[0]+1, 0]
            else:
                if mid[1]>0:
                    r = [mid[0],mid[1] - 1]
                else:
                    r = [mid[0]-1, col - 1]
        return False        
    
    
    
#    # approach 1 - flatten and then binary search
#    def binarySearch(self, nums, target):
#         l = 0
#         r = len(nums) - 1
#         while(l<=r):
#             mid = int((l+r) / 2)
#             if nums[mid] == target:
#                 return True
#             elif nums[mid] > target:
#                 r = mid - 1
#             else:
#                 l = mid + 1
#         return False
    
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         nums = []
#         for i in matrix:
#             for j in i:
#                 # print(j)
#                 nums.append(j)
#         return self.binarySearch(nums, target)