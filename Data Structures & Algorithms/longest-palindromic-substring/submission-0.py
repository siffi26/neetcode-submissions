class Solution:
    def longestPalindrome(self, s: str) -> str:
        # For every possible center:

        # expand left 
        # expand right

        # while left == right:
        #     keep growing

        # also palindrome could be odd or even length, hence expand(i,i) and expand(i, i+1)

        res = ""

        def expand(l, r):
            nonlocal res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(res):
                    res = s[l:r + 1]
                l -= 1
                r += 1
        for i in range(len(s)):
            expand(i, i)       # odd length palindrome
            expand(i, i + 1)   # even length palindrome
        return res
        
        