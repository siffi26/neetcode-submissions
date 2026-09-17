# Two Sum - Two Pointers with Sorting
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {}
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in prevmap:
                return [prevmap[diff], i]
                
            prevmap[nums[i]] = i

            
