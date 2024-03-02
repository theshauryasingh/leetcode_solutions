class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero = -1
        for i, num in enumerate(nums):
            if num == 0:
                if zero != -1:
                    return [0]*len(nums)
                zero = i
            else:
                product = product * num
        finalProduct = []
        if zero>-1:
            for i in range(len(nums)):
                if i == zero:
                    finalProduct.append(product)
                else:
                    finalProduct.append(0)
        else:
            for i in range(len(nums)):
                finalProduct.append(int(product/nums[i]))
        return finalProduct