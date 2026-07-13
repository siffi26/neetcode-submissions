"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Since now Interval is a class, not list
        if not intervals:
            return True

        # Sort Interval objects by start time
        intervals.sort(key=lambda interval: interval.start)
        prev_end = intervals[0].end

        for each in intervals[1:]:
            curr_start = each.start
            curr_end = each.end

            if curr_start < prev_end:
                return False
            
            # No conflict; move to the current meeting
            prev_end = curr_end
            
        return True