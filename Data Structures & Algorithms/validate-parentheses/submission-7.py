class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {"[": "]", "{": "}", "(": ")"}

        stack=[]
        for c in s:
            if c in ["[", "{", "("]:
                stack.append(c)
            else:
                if len(stack)==0:
                    return False

                top = stack[-1]
                if hmap[top] == c:
                    stack.pop()
                else:
                    return False
            

        if len(stack)==0:
            return True
        else:
            return False