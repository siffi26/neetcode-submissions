class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # either include number or not
        result = []
        subset = [] # stack for mainatining include/exclude

        def dfs(index):
            # Finished making decisions
            if index == len(nums):
                result.append(subset[:])
                return

            # Include current number
            subset.append(nums[index])
            dfs(index + 1)

            # Undo
            subset.pop()

            # Don't include current number
            dfs(index + 1)

        dfs(0)
        return result



        