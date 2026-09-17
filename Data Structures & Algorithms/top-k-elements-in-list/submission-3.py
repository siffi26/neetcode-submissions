import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashMap = {}
        for num in nums:
            hashMap[num] = 1 + hashMap.get(num, 0)

        # {1:1, 2:2, 3:3, 7:2}

        heap = []
        cnt = 0
        for num, counts in hashMap.items():
            if cnt < k:
                heapq.heappush(heap, (counts, num))
                cnt+=1
            else:
                if counts > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (counts, num))
        ans = []
        for each in heap:
            ans.append(each[1])

        return ans



        

