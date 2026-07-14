class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    # Try a starting station
    # Keep updating remaining tank
    # If tank becomes negative → this start fails
    # Move start forward and try again
    # If all n edges are crossed → return start

        n = len(gas)

        for start in range(n):
            tank = 0
            completed = True

            for step in range(n):
                # IMP: The % n here wraps around the circle
                i = (start + step) % n 

                tank += gas[i]
                tank -= cost[i]

                if tank < 0:
                    completed = False
                    break

            if completed:
                return start

        return -1


        