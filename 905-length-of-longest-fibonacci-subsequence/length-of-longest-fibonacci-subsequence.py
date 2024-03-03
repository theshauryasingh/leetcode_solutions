# #input
# [1,3,5]
# [1,2,3,4,5,6,7,8]
# [1,3,7,11,12,14,18]

## Attempt I - brute force:
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        best = 0
        s = set(arr)
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                count = 1
                a = arr[i]
                b = arr[j]
                while(b in s):
                    a,b = b, a+b
                    count += 1
                best = max(best, count)
        if best>= 3:
            return best
        return 0