class Solution:
    def rob(self, nums: List[int]) -> int:
        # Since first and last houses are neighbors,
        # we cannot rob both.
        #
        # Solve two linear House Robber problems:
        # 1. Exclude last house  -> nums[:-1]
        # 2. Exclude first house -> nums[1:]
        #
        # Return the better of the two.

        if len(nums) == 1:
            return nums[0]

        def robLinear(arr):
            # dp(i) = maximum money we can rob from houses 0...i

            # dp(i) = max(
            #     dp(i-1),           # Skip current house
            #     dp(i-2) + arr[i]   # Rob current house
            # )

            n = len(arr)

            if n == 1:
                return arr[0]

            dp = [0] * n

            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, n):
                dp[i] = max(
                    dp[i - 1],
                    dp[i - 2] + arr[i]
                )

            return dp[n - 1]

        return max(
            robLinear(nums[:-1]),
            robLinear(nums[1:])
        )