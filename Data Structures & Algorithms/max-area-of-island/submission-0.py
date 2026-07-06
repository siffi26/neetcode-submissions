class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = self.dfs(grid, i, j, n, m)
                    res = max(res, area)

        return res

    def dfs(self, grid: List[List[str]], i:int, j: int, n:int, m:int):
        if i < 0 or i >= n or j < 0 or j >= m:
            return 0
        
        if grid[i][j] == 0:
            return 0

        # most powerful for saving time O(n*m) complexity and no DP required 
        grid[i][j] = 0
        area = 1

        area += self.dfs(grid, i - 1, j, n, m)   # up
        area += self.dfs(grid, i + 1, j, n, m)   # down
        area += self.dfs(grid, i, j - 1, n, m)   # left
        area += self.dfs(grid, i, j + 1, n, m)   # right
        return area
   
        