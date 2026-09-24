class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hset = set()
        i=0
        res = 0
        for j in range(len(s)):
            while s[j] in hset: # upto repeated char
                hset.remove(s[i]) #remove from left side
                i+=1
            curr_len = j-i+1
            res = max(curr_len, res)

            hset.add(s[j])
            
        return res





