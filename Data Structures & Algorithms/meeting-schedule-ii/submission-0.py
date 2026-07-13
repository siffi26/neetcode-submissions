import heapq
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x:x.start)
        # End times of meetings currently using rooms
        rooms = []

        for interval in intervals:
            # Earliest room is available
            if rooms and interval.start >= rooms[0]:
                heapq.heappop(rooms)
            
            # Assign current meeting to a room
            heapq.heappush(rooms, interval.end)
        
        return len(rooms)


        