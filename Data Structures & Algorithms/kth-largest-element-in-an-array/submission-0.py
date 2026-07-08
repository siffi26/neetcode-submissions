import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = [-each for each in nums]
        heapq.heapify(heap)
        print(heap)

        l = 1
        res = 0
        while heap and l<=k:
            res = heapq.heappop(heap)
            l+=1
        return -res





        