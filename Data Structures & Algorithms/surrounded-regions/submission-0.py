class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # start from the borders, call dfs from the borders.
        # mark as T if it the path starting from border using DFS
        # then convert T to O (back to original), and 
        # remaining O will be enclosed, so convert to 'X'

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):
            # Outside the board
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # Only process O cells
            if board[r][c] != "O":
                return

            # Temporarily mark this O as safe
            board[r][c] = "T"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Check O cells on left and right borders
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        # Check O cells on top and bottom borders
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # Capture surrounded regions and restore safe regions
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"