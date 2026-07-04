class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        l = 0
        r = (m*n)-1
        while(l<=r):
            mid = (l+r)//2
            row = mid//m
            col = mid%m

            if matrix[row][col] == target:
                return True
            elif target > matrix[row][col]:
                l = mid+1
            elif target < matrix[row][col]:
                r = mid-1
        return False
