# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # do queue bfs/dfs and check if 
        # root > root.left and root < root.right for all subtree
        if root is None:
            return True

        # (root, -∞, +∞)
        # every queue entry needs to remember
        # curr, smallest value it is allowed to have (lower)
        # the largest value allowed to have (upper)
        queue = deque([
            (root, float("-inf"), float("inf"))
        ])

        while queue:
            curr, lower, upper = queue.popleft()

            if not (lower < curr.val < upper):
                return False

            if curr.left:
                queue.append(
                    (curr.left, lower, curr.val)
                )

            if curr.right:
                queue.append(
                    (curr.right, curr.val, upper)
                )

        return True