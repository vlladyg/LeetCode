class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_set = set()
            for j in range(9):
                if board[i][j] in row_set:
                    return False
                elif board[i][j] != '.':
                    row_set.add(board[i][j])
        
        for j in range(9):
            col_set = set()
            for i in range(9):
                if board[i][j] in col_set:
                    return False
                elif board[i][j] != '.':
                    col_set.add(board[i][j])
        
        for ii in range(3):
            for jj in range(3):
                sub_set = set()
                for i in range(3):
                    for j in range(3):
                        if board[ii*3 + i][jj*3 + j] in sub_set:
                            return False
                        elif board[ii*3 + i][jj*3 + j] != '.':
                            sub_set.add(board[ii*3 + i][jj*3 + j])

        return True
