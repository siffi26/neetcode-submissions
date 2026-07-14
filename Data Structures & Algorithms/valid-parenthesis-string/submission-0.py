class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack = []
        star_stack = []

        for i, ch in enumerate(s):
            if ch == "(":
                open_stack.append(i)

            elif ch == "*":
                star_stack.append(i)

            else:  # ')'
                if open_stack:
                    open_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False

        # Match remaining '(' with later '*'
        while open_stack and star_stack:
            open_index = open_stack.pop()
            star_index = star_stack.pop()

            # '*' must come after '(' to act as ')'
            if open_index > star_index:
                return False

        return not open_stack
        