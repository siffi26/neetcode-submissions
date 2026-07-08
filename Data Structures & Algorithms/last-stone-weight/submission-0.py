import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # lets make max heap, intuition: when sorting is needed again and again

        heap = []
        n = len(stones)

        for num in stones:
            heapq.heappush(heap, -num)

        while len(heap)>1:
            ele1 = heapq.heappop(heap)
            ele2 = heapq.heappop(heap)
            if ele1 != ele2:
                subs = (-ele1) - (-ele2)
                heapq.heappush(heap, -subs)
        if len(heap) == 1:
            return -heap[0]
        else:
            return 0
            



        