class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()
        res = ""
        for c in s:
            if c.isalnum():
                res+=c

        print(res)

        i, j= 0, len(res)-1

        while(i<=j):
            if res[i]==res[j]:
                i+=1
                j-=1
            else:
                return False
        return True