class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            False
        seen = []
        for i in nums:
            if i in seen:
                return True
            else:
                seen.append(i)
        return False


