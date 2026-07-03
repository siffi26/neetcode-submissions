# Two Sum - Two Pointers with Sorting
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # have I seen the diff of current element in elements previously seen
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

            
