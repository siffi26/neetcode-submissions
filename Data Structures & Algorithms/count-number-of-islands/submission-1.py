class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ans = 0
        n = len(grid)
        m = len(grid[0])

        def cntIslands(i, j):
            if i<0 or i>=n or j<0 or j>=m:
                return

            if grid[i][j] == "0":
                return

            grid[i][j] = "0"
            
            cntIslands(i, j+1)
            cntIslands(i+1, j)
            cntIslands(i-1, j)
            cntIslands(i, j-1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    cntIslands(i, j)
                    ans+=1

        return ans



        