# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal diameter  # to be able to update variable
            if node == None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            diameter = max(diameter, left+right)
            # at each node, the diameter would be sum of left nodes+right nodes
            # take max as we traverse all nodes
            #     A
            #    / \
            #   B   C
            #  / \
            # D   E

            # The path connecting them is: D → B → A → C
            return 1 + max(left, right)


        dfs(root)
        return diameter


        