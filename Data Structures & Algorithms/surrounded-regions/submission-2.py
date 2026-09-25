class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])

        queue = deque()

        for i in range(n):
            for j in range(m):
                if (i==0 or i==n-1 or j==0 or j==m-1) and board[i][j]=="O":
                    board[i][j] = "T"
                    queue.append((i,j))

        # find all 0 connected to boundary ones, they cannot change too
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        while queue:
            i, j = queue.popleft()

            for di, dj in directions:
                ni = i+ di
                nj = j+ dj

                if ni<0 or ni>=n or nj<0 or nj>=m:
                    continue

                if board[ni][nj] == "T":
                    continue

                if board[ni][nj] == "O":
                    board[ni][nj] = "T"
                    queue.append((ni, nj))
                
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"

                elif board[i][j] == "T":
                    board[i][j] = "O"




                    









