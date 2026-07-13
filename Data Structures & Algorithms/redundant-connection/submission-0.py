from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges):

        graph = defaultdict(list) # don't create graph in beginning

        def dfs(node, target, visited):

            if node == target:
                return True

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor, target, visited):
                        return True

            return False

        for u, v in edges:
            visited = set()
            if u in graph and v in graph:
                if dfs(u, v, visited):
                    return [u, v]
            # create graph now after looking at visited set from DFS
            graph[u].append(v) 
            graph[v].append(u)