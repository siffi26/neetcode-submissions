class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # sort the list
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet: # maybe if less than 1 is not there, maybe high be there
                length = 1
                while (num + length) in numSet: #then keep going forward in numSet
                    length += 1
                longest = max(length, longest)
        return longest