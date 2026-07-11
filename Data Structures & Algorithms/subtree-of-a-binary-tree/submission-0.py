# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(
        self,
        root: Optional[TreeNode],
        subRoot: Optional[TreeNode]
    ) -> bool:

        def sameTree(node1, node2):
            # Both ended at the same time
            if node1 is None and node2 is None:
                return True

            # Only one ended, so structures differ
            if node1 is None or node2 is None:
                return False

            # Values differ
            if node1.val != node2.val:
                return False

            return (
                sameTree(node1.left, node2.left)
                and sameTree(node1.right, node2.right)
            )


class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(Node1: Optional[TreeNode], Node2: Optional[TreeNode]):
            if Node1 == None and Node2 == None:
                return True
            if Node1 == None or Node2 == None:
                return False

            if Node1.val != Node2.val:
                return False
            
            if Node1.val == Node2.val:
                return (dfs(Node1.left, Node2.left) and dfs(Node1.right, Node2.right))

        if subRoot == None:
            return True
        
        if root == None:
            return False

        if dfs(root, subRoot): # this is our final function call with dfs
            return True

        # since the second one is a subtree, cannot have same root
        # so we check if just immediate children of root is subroot
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

            



        