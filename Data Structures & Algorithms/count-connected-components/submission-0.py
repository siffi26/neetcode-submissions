class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        visited = []
        components = 0

        def dfs(node):
            visited.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        # final call   
        for node in range(n):
            # at start all nodes are not visited
            if node not in visited:
                components += 1
                dfs(node)
        
        return components
        