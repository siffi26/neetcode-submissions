from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # start from rotten banana, check all directions, 
        # time: if in all directions, there is any even one banana (1 value), 
        # then inc time+1
        # if not, return -1

        total_time = -1
        directions = [
            [0, 1],
            [1, 0],
            [0, -1], 
            [-1, 0]
        ]
        n = len(grid)
        m = len(grid[0])

        queue = deque()
        fresh_count = 0
        minutes = 0

        # Find every initially rotten fruit and count fresh fruits
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        print(queue)

        while queue and fresh_count>0:
            level_size = len(queue)
            for _ in range(level_size):
                r, c = queue.popleft()
                for dr, dc in directions:
                    new_r = r+dr
                    new_c = c+dc

                    if new_r>=n or new_c>=m or new_r<0 or new_c<0:
                        continue

                    # Only process fresh fruit
                    if grid[new_r][new_c] != 1:
                        continue

                    # Make the fresh fruit rotten
                    grid[new_r][new_c] = 2
                    fresh_count -= 1
                    queue.append((new_r, new_c))
            minutes+=1
        if fresh_count > 0:
            return -1
        return minutes
        
