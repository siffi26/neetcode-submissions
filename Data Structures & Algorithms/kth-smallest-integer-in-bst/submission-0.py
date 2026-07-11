# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Inorder traversal of a BST gives values in sorted order.
        stack = []
        current = root
        count = 0

        while current or stack:

            # Go as far left as possible
            while current:
                stack.append(current)
                current = current.left

            # Visit the smallest remaining node
            current = stack.pop()
            count += 1

            if count == k:
                return current.val

            # Then explore its right subtree
            current = current.right
        