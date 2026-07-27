class Solution:
    def countBits(self, n: int) -> List[int]:
        # number of times you divide any integer by 2 is log(n)
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            num = i
            while num != 0:
                res[i] += 1
                num &= (num - 1)
        return res