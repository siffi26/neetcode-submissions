class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Standing on stair i, you pay cost[i] once, and then can move either 1 or 2 stairs.

        # dp(i) = min(
            # dp(i-1) + cost[i-1], here dp(i-1) is sum of cost to reach i-1
            # dp(i-2) + cost[i-2]) # and then to reach dp[i] we pay exit cost at (i-1) or (i-2) to get to dp[i] added to prev cost
        
        memo = {}

        def dfs(i):
            if i == 0: # cost to exit stair 0
                return 0
            if i == 1: # cost to exit stair 0
                return 0

            if i in memo: 
                return memo[i] # save prev costs

            memo[i] = min(
                dfs(i - 1) + cost[i - 1], 
                dfs(i - 2) + cost[i - 2]
            )
            return memo[i]
        
        # to compute for top of cost list, which would be index = len(cost)
        return dfs(len(cost))
            
            



