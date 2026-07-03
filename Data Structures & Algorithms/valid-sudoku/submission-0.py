from typing import List
import numpy as np

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Convert to numpy array with 0s for dots
        board_new = np.array([[int(char) if char != '.' else 0 for char in row] for row in board])
        
        # 1. Row and Column Checks
        for i in range(9):
            # Row check: Filter out zeros, then check uniqueness
            row_elements = [num for num in board_new[i] if num != 0]
            if len(set(row_elements)) != len(row_elements):
                return False
                
            # Column check: Use board_new[:, i] to grab the column, filter zeros
            col_elements = [num for num in board_new[:, i] if num != 0]
            if len(set(col_elements)) != len(col_elements):
                return False

        # 2. 3x3 Block Checks
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                block = board_new[r:r+3, c:c+3]  # Fixed variable name here
                filled_elements = [num for num in block.flatten() if num != 0]
                if len(set(filled_elements)) != len(filled_elements):
                    return False
                    
        return True