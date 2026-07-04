class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        com_array = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
               com_array.append(matrix[i][j])

        l = 0
        r = len(com_array) - 1
        
        while l<=r:
            m = (l+r)//2
            if target == com_array[m]:
                return True
            elif target>com_array[m]:
                l = m+1
            elif target<com_array[m]:
                r = m-1
        return False


        