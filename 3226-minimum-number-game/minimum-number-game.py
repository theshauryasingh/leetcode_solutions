class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        heap = []
        for items in nums: #heapify O(n)
            heapq.heappush(heap, items) #insertion O(log n)
        # overall O(n logn)
        while(len(heap) > 0): #iteration O(n)
            a = heapq.heappop(heap) #deletion O(log n)
            b = heapq.heappop(heap) #deletion O(log n)
            arr.append(b) #insertion at end O(1)
            arr.append(a) #insertion at end O(1)
        # overall O(n logn)
        return arr
        