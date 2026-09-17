class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])

        queue = deque()

        # if border "0" then not change border so mark them as 'T'
        for i in range(n):
            for j in range(m):
                if (board[i][j] == "O"
                    and (i == 0 or i == n-1 or j == 0 or j == m-1)):
                    
                    queue.append((i, j))
                    board[i][j] = "T"
            
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # Find all O's connected to border O's
        while queue:
            i, j = queue.popleft()
            for di, dj in directions:
                ni = i+di
                nj = j+dj

                # mark all "0" connected to border as "T"
                if (ni>=0 and ni<n and nj>=0 and nj<m and board[ni][nj]=="O"): 
                    board[ni][nj]="T"
                    queue.append((ni, nj))



        # Flip surrounded O's
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"



                







