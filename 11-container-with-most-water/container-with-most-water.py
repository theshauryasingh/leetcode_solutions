class Solution:
    def maxArea(self, height: List[int]) -> int:
        # height = [1,8,6,2,5,4,8,3,7]
        left = 0
        right = len(height)-1
        maxWater = 0
        while(left<right):
            print(left, right)
            water = min(height[left], height[right]) * (right-left)
            if water > maxWater:
                maxWater = water
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxWater
    
## approach 1 - brute force
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         # height = [1,8,6,2,5,4,8,3,7]
#         maxWater = 0
#         for i, val1 in enumerate(height):
#             for j, val2 in enumerate(height):
#                 water = min(val1, val2) * abs(i-j)
#                 if water > maxWater:
#                     maxWater = water
#         return maxWater