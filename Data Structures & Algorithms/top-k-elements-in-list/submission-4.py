import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for each in nums:
            hmap[each] = 1+ hmap.get(each, 0)

        heap = []
        for key,value in hmap.items():
            heapq.heappush(heap, (value, key))

            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for each in heap:
            res.append(each[1])

        return res
            


