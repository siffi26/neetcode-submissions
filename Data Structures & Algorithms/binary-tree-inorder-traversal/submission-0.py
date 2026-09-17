# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def traversal(root: Optional[TreeNode]):
            if root == None:
                return

            traversal(root.left)
            ans.append(root.val)
            traversal(root.right)
        
        traversal(root)
        return ans

        
            

        