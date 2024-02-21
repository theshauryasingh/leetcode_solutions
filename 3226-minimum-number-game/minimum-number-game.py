class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        heap = []
        for items in nums:
            heapq.heappush(heap, items)
        
        while(len(heap) > 0):
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            arr.append(b)
            arr.append(a)
            print(a, b)
        print(arr)
        return arr
        