class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for i in range(len(s)):
            if stack and s[i] in closeToOpen and stack[-1] == closeToOpen[s[i]]:
                stack.pop()
            else:
                stack.append(s[i])
        print(stack)

        if len(stack) == 0:
            return True
        else:
            return False
        