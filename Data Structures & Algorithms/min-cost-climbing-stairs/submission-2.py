class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # at n = reach by either n-1 or n-2 th stairs
        # cost[n] = min(cost[n-1], cost[n-2])
        rcost = [0] * len(cost)
        
        rcost[0] = cost[0]
        rcost[1] = cost[1]

        n = len(cost)
        for i in range(2, n):
            rcost[i] = min(rcost[i-1], rcost[i-2]) + cost[i]

        return min(rcost[n-1], rcost[n-2])

