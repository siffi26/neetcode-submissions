class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        merged = []
        merged.append(intervals[0])

        for curr_start, curr_end in intervals[1:]:
            # "prev inside loop" of "merged" list
            prev_start, prev_end = merged[-1]
            if prev_end >= curr_start:
                merged[-1][1] = max(prev_end, curr_end)
            else:
                merged.append([curr_start, curr_end])

        return merged



