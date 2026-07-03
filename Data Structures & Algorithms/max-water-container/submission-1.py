class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        
        res = 0
        while i<j:
            dist_bw = j-i
            curr_height = min(heights[i], heights[j])
            vol = dist_bw * curr_height
            res = max(res, vol)
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
            
        return res


        