class Solution:
    def hammingWeight(self, n: int) -> int:
        # every time we do: n = n & (n - 1) we eliminate exactly one 1 bit
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res

        