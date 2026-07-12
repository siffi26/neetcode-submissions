class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree with n nodes must have exactly n - 1 edges.
        if len(edges) != n - 1:
            return False

        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for neighbor in graph[node]:
                # Ignore the edge we came from
                if neighbor == parent:
                    continue
                # Found another way to a visited node
                if neighbor in visited:
                    return False
                if not dfs(neighbor, node):
                    return False
            return True

        # Detect cycle
        if not dfs(0, -1):
            return False

        # Check connectivity
        return len(visited) == n
    