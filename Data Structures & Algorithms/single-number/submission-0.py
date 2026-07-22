class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Bit Manipulation (XOR) - The optimal solution relies on XOR properties: a ^ a = 0 and a ^ 0 = a
        res = 0
        for num in nums:
            res = num ^ res
        return res
        