class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        h_set = set()
        ans = 0

        for j in range(len(s)):
            while s[j] in h_set:
                h_set.remove(s[i])
                i += 1

            h_set.add(s[j])
            
            ans = max((j-i+1), ans)
            j+=1
        
        return ans



