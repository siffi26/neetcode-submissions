class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return False

        s = s.lower()
        s = "".join(c for c in s if c.isalnum())
        print(s)
        i = 0
        j = len(s)-1

        while i<j:
            if s[i] != s[j]:
                return False
            else:
                i+=1
                j-=1
        return True

            
    