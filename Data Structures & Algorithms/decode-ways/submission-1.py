class Solution:
    def numDecodings(self, s: str) -> int:
        # only max two digits mapping possible
        # "1" → "A", "2" → "B", …, "26" → "Z"

        # At any index i, either Take one digit (s[i]) → valid if it’s not '0'
        # or Take two digits (s[i:i+2]) → valid if it forms a number between 10 and 26

        dp = {len(s): 1}
        ## Equivalent to: dp = [0] * (len(s) + 1)
        ## dp[len(s)] = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                dp[i] += dp[i + 2]
                
        return dp[0]

