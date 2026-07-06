"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # Node(
        #    val=2,
        #     neighbors=[Node1, Node3]
        # )
        # graphs need a visited map - Hashmap

        if node is None:
            return None
        visited = {}
        return self.dfs(node, visited)
        

    def dfs(self, node, visited):
        if node in visited:
            return visited[node]
        
        copy = Node(node.val)
        visited[node] = copy

        for neighbor in node.neighbors:
            clonedNeighbor = self.dfs(neighbor, visited)
            copy.neighbors.append(clonedNeighbor)
        return copy
        
        