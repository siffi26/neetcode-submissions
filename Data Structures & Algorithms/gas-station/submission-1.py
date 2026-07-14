class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # So if starting from 2 couldn't make it past 5, then starting from 3 definitely can't.
        # If total gas is less than total cost, completing the circuit is impossible
        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = 0

        for i in range(len(gas)):
            # Fill gas at current station and spend gas to reach the next station
            tank += gas[i] - cost[i]

            # Can't reach the next station from the current starting point
            if tank < 0:
                # Skip all stations from 'start' to 'i'
                start = i + 1
                tank = 0

        return start