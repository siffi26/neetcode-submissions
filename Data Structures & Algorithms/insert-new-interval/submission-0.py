class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        # since it is sorted
        for i, each in enumerate(intervals):
            curr_start, curr_end = each[0], each[1]
            new_start, new_end = newInterval[0], newInterval[1]

            # Current interval is completely after newInterval
            if new_end < curr_start:
                res.append(newInterval)
                # Remaining intervals are already sorted
                res.extend(intervals[i:])
                return res
            
            # Current interval is completely before newInterval
            elif new_start > curr_end:
                res.append(each) # keep iterating until we can insert newInterval
            
            # if there is overlap
            else:
                newInterval = [
                    min(curr_start, new_start),
                    max(curr_end, new_end)
                ] 
        
        # newInterval belongs at the end
        res.append(newInterval)

        return res

            

