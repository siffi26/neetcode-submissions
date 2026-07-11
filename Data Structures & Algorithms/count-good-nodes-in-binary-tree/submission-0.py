from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # greater than or equal to the maximum value seen on its path
        count = 0
        queue = deque()
        queue = deque([(root, root.val)])

        root_value = root.val
        while queue:
            node, path_max = queue.popleft()
            if node.val >= path_max:
                count += 1

            new_max = max(path_max, node.val)

            if node.left:
                queue.append((node.left, new_max))

            if node.right:
                queue.append((node.right, new_max))

        return count

                




        