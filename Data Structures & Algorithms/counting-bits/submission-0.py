class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        offset = 1

        # number of times you divide any integer by 2 is log(n)
        # here we do DP, where most significant bit happends, like at 2, 4, 8,...
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
        