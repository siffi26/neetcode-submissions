class Solution:
    def jump(self, nums: List[int]) -> int:
        # BFS: each “level” represents all positions we can reach using the same number of jumps
        # from those positions, we compute how far we can reach in one more jump

        farthest = 0
        left = right = 0
        count = 0

        while right<len(nums)-1:
            farthest = 0
            for i in range(left, right+1):
                farthest = max(farthest, i+nums[i])

            left = right
            right = farthest
            count+=1

        return count
 