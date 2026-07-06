class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counts = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    counts = counts+1
                    self.dfs(grid, i, j, n, m)
        return counts

    def dfs(self, grid: List[List[str]], i:int, j: int, n:int, m:int):
        if i < 0 or i >= n or j < 0 or j >= m:
            return
        
        if grid[i][j] == "0":
            return
        
        grid[i][j] = "0"

        self.dfs(grid, i - 1, j, n, m)   # up
        self.dfs(grid, i + 1, j, n, m)   # down
        self.dfs(grid, i, j - 1, n, m)   # left
        self.dfs(grid, i, j + 1, n, m)   # right




        