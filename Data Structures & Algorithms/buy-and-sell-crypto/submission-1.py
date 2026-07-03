class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1 # the two pointers doesn't have to be start and end pos, it can be consecutive
        maxP = 0

        while j<len(prices):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                maxP = max(maxP, profit)
            else:
                i = j
            j+=1
        return maxP
