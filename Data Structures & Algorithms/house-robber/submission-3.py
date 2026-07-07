class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp(i) = maximum money we can rob from houses 0...i

        # dp(i) = max(
        #     dp(i-1),
        #     dp(i-2) + nums[i]
        # )
        
        if len(nums) ==1:
            return nums[0]

        elif len(nums)>=1:
            n = len(nums)
            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            
            return dp[n-1]



