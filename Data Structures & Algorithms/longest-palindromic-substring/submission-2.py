class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        def expand(i: int, j:int) -> str:
            nonlocal res
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1 # starting at middle, and expanding
                j+=1
                
            palindrome = s[i + 1:j]
            if len(palindrome)>len(res):
                res=palindrome

        for i in range(len(s)):
            expand(i, i) #odd length
            expand(i, i+1) #even length
        
        return res

            

        
        