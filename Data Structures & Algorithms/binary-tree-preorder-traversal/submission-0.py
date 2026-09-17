# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # preorder = left, root, right

        ans = []

        def traversal(root: Optional[TreeNode]):
            if root == None:
                return

            ans.append(root.val)   # root
            traversal(root.left)   # left
            traversal(root.right)  # right

        traversal(root)
        return ans




        