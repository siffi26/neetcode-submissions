class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # two decisions go down or go right, and there
        # is coordinated where we can repeatedly come to from
        # either right or down, hence we need to cache it cache[r][c]
        # as DFS is very expensive

        # compute for each square close to Finish, means you
        # can compute for start position res = R + D

        # what is the base case, from Finish pos, 
        # we define way to get to itself is 1.

        # by default define all other cells as 0. 
        # start from pos left of finish, for it, sum of R+D will be 1+0.

        # set out of bounds, now lets compute from each bottom row

        row = [1] * n
        for i in range(m-1):
            newRow = [1] * n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]






        