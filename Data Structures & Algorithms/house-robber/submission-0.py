class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp(i) = maximum money we can rob from houses 0...i

        # dp(i) = max(
        #     dp(i-1),
        #     dp(i-2) + nums[i]
        # )
        memo = {}

        def dfs(i: int):
            if i == 0:
                return nums[0]

            if i == 1:
                return max(nums[0], nums[1])

            if i in memo:
                return memo[i]

            memo[i] = max(dfs(i-1), (dfs(i-2)+nums[i]))
            return memo[i]

        n = len(nums)-1
        return dfs(n)



        