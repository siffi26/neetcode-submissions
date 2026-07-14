class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        max_sum = nums[0] 
        current_sum = nums[0]
        i = 0

        # At each index, we have two choices
        # either add the current element to curSum 
        # or start a new subarray by resetting curSum

        for num in nums[1:]: 
            # Continue the old subarray or start a new one
            current_sum = max(num, current_sum + num)

             # Record the best sum found
            max_sum = max(max_sum, current_sum)

        return max_sum






        