class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort first
        intervals.sort()
        prev_start, prev_end = intervals[0]
        count = 0

        for curr_start, curr_end in intervals[1:]:

            if curr_start >= prev_end:
                prev_start, prev_end  = curr_start, curr_end

            else:
                count+=1
                # Keep the interval with the smaller end
                if curr_end < prev_end:
                    prev_start, prev_end = curr_start, curr_end
        return count



        