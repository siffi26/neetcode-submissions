class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # for every 0, do bfs (layer 1, immediate neighbour), .. and keep updating cells

        n = len(grid)
        m = len(grid[0])

        queue = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                     queue.append((i, j))
        
        directions = [
            (-1, 0),  # up
            (1, 0),   # down
            (0, -1),  # left
            (0, 1)    # right
        ]

        while queue:
            r, c = queue.popleft()
            #iterate in all directions, top down, left right
            for dr, dc in directions:
                new_r, new_c = r+dr, c+dc

                # Boundary check
                if (new_r < 0 or new_r >= n or
                    new_c < 0 or new_c >= m):
                    continue

                # Skip water (-1) and already-visited cells, hence check anything other than big number
                if grid[new_r][new_c] != 2147483647:
                    continue
                
                # Update distance
                grid[new_r][new_c] = grid[r][c] + 1

                # IMP: if you're wondering then how would paths value increase, hence we add new ele to queue to come back here
                # Treasures update distance-1 cells.
                # Distance-1 cells are added to the queue.
                # Then distance-1 cells update distance-2 cells.
                # Then distance-2 cells update distance-3 cells.

                queue.append((new_r, new_c))






        