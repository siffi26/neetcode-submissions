class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        def expand(i: int, j:int):
            nonlocal res
            while i>=0 and j<len(s) and s[i]==s[j]:
                curr_s = s[i:j+1]
                if len(curr_s) > len(res):
                    res = curr_s
                i-=1
                j+=1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i+1)

        return res


            

        
        