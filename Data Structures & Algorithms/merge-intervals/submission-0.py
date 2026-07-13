class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start time
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for curr_start, curr_end in intervals[1:]:
            prev_start, prev_end = merged[-1]
            
            # if overlap menas start of curr < end of prev value
            if curr_start <= prev_end:
                # update our result (merged) array to correct end value
                merged[-1][1] = max(prev_end, curr_end)
            
            else:
                merged.append([curr_start, curr_end])
        return merged





        