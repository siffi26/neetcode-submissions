class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # from that cell to both the Pacific and Atlantic oceans
        # Start DFS/BFS from the Pacific borders and walk only to 
        # neighbors that are greater than or equal to the current height.
        n = len(heights)
        m = len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [
            [0, 1], [1, 0],
            [0, -1], [-1, 0]
        ]

        def dfs(r, c, visited):
            visited.add((r, c))

            for dr, dc in directions:
                new_r = r+dr
                new_c = c+dc

                # Check boundaries
                if (
                    new_r < 0 or new_r >= n or
                    new_c < 0 or new_c >= m
                ):
                    continue

                # Avoid processing the same cell again
                if (new_r, new_c) in visited:
                    continue

                # Move from current cell to equal or higher cell
                if heights[new_r][new_c] < heights[r][c]:
                    continue
                
                dfs(new_r, new_c, visited)


        # Pacific: top row and left column
        for c in range(m):
            dfs(0, c, pacific)

        for r in range(n):
            dfs(r, 0, pacific)

        # Atlantic: bottom row and right column
        for c in range(m):
            dfs(n - 1, c, atlantic)

        for r in range(n):
            dfs(r, m - 1, atlantic)

        result = []
        for r in range(n):
            for c in range(m):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])
        return result
