# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # three things must be true:
            # Current node values are the same
            # Left subtrees are the same
            # Right subtrees are the same

        def dfs(nodep: Optional[TreeNode], nodeq: Optional[TreeNode]) -> int:
            if nodep == None and nodeq == None:
                return True

            if nodep == None and nodeq != None:
                return False

            if nodep != None and nodeq == None:
                return False

            if nodep.val != nodeq.val:
                return False

            return (dfs(nodep.left, nodeq.left) and dfs(nodep.right, nodeq.right))

        return dfs(p, q)