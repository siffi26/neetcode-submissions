class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {} # we create function inside (dfs) because memo dict is outside

        def dfs(n):
            if n == 0:
                return 1
            if n == 1:
                return 1
            
            if n in memo:
                return memo[n]

            memo[n]= dfs(n-1) + dfs(n-2)
            return memo[n]
        return dfs(n)
        