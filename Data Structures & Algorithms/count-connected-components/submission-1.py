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

            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)

        for node in range(n):
            if node not in visited:
                components+=1
                dfs(node)

        return components