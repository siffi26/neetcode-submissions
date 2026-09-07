class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # replacements needed = window length - count of most frequent character
        counts = {}
        left = 0
        max_freq = 0
        ans = 0

        for right in range(len(s)):
            c = s[right]
             
            counts[c] = counts.get(c, 0) + 1
            max_freq = max(max_freq, counts[c])

            while (right-left+1) - max_freq > k:
                counts[s[left]]-=1
                left+=1

            ans = max(ans, right-left+1)

        return ans



        
        

        
        