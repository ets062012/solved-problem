class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_placement(value, row, col):
         
            if any(board[row][c] == value for c in range(9) if c != col):
                return False

            if any(board[r][col] == value for r in range(9) if r != row):
                return False

          
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            if any(board[r][c] == value for r in range(start_row, start_row + 3) for c in range(start_col, start_col + 3) if (r, c) != (row, col)):
                return False

            return True

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if not is_valid_placement(board[i][j], i, j):
                        return False

        return True
