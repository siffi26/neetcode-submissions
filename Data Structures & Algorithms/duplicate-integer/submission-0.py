class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_nums = list(set(nums))
        # print(new_nums)
        if len(new_nums) == len(nums):
            return False
        else:
            return True
        