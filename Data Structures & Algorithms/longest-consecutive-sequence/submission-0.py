class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums) # sorted it, so we can start with smallest number
        res = 0
        for num in nums:
            streak, curr = 0, num
            while curr in store: # check if +1 incremented number is in list
                streak+=1
                curr+=1
            res = max(res, streak)
        return res
