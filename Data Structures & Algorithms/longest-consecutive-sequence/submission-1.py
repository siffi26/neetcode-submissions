class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = sorted(nums)
        res = 0
        for num in nums:
            streak = 0
            curr = num
            while curr in store:
                streak+=1
                curr+=1
            res = max(streak, res)
        return res
