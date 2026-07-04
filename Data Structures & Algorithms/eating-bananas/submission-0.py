class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = r

        while(l<=r):
            k = (l+r)//2
            hours = 0
            for pile in piles:
                # since with (pile//k)+1 we might end up adding 1 even when we shouldn't 
                hours += (pile + k - 1) // k
            
            if hours<=h:
                # to find least value we don't return straight away
                ans = k
                r = k-1
            elif hours>h:
                l = k+1
        return ans
        


        
        