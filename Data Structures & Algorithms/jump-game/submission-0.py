class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # instead of choosing how much to jump
        # keep track of the furthest index you can currently reach

        farthest = 0

        for i in range(len(nums)):
            # if can't reach curr pos
            if i > farthest:
                return False

            # calculate farthest you can go
            # farthest tracks prev max for you
            farthest = max(farthest, i+nums[i])

            if farthest >= len(nums)-1:
                return True
        
        return True
