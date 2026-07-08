from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n:int) -> int:
        # How is this heap? Run the task with the highest remaining frequency
        # The heap only relies on frequency so we don't store values

        counts = Counter(tasks)

        heap = [-each for each in counts.values()]
        # heap = []
        heapq.heapify(heap) # this will update in-place

        q = deque() # to keep track of [counts, hold_time]
        time = 0

        while heap or q:
            time+=1

            if heap:
                cnt = heapq.heappop(heap) 
                cnt+=1 # since cnt is negative, basically reduce cnt

                if cnt:
                    q.append([cnt, time+n]) 

            # if time is equal to second ele in queue, we check "Can we use it?""
            if q and q[0][1]==time:
                cnt, ready_time = q.popleft() 
                # after hold time, you put back ele "A" back into heap, so we can put it in final sequence
                heapq.heappush(heap, cnt)

        return time








        