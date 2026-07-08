class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}

        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1

        heap = []

        for key, value in hmap.items():
            # heap stores: (frequency, number)
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
            else:
                minFreq = heap[0]   # smallest frequency tuple

                if value > minFreq[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (value, key))

        output = []
        for freq, num in heap:
            output.append(num)

        return output