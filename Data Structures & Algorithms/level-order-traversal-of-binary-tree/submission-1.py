from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        ans = []

        queue = deque()
        queue.append(root)

        while queue:
            qlen = len(queue)
            ele = []

            for i in range(qlen):
                e = queue.popleft()
                ele.append(e.val)

                if e.left:
                    queue.append(e.left)

                if e.right:
                    queue.append(e.right)

            ans.append(ele)

        return ans


