class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        out = 0
        flag = False
        flag_pawn = False
        for i in range(8):
            if not flag:
                flag_pawn = False
                for j in range(8):
                    if board[i][j] == 'p' and not flag:
                        flag_pawn = True
                    if flag_pawn and board[i][j] == 'B':
                        flag_pawn = False
                    if board[i][j] == 'R':
                        if flag_pawn:
                            out += 1
                            flag_pawn = False

                        flag = True
                        ii = i
                        jj = j

                    if board[i][j] == 'p' and flag:
                        out += 1
                        break
                    if board[i][j] == 'B' and flag:
                        break
                    
            else:
                break

        for i in range(ii+1, 8):
            if board[i][jj] == 'B':
                break
            if board[i][jj] == 'p':
                out += 1
                break

        for i in range(ii - 1, -1, -1):
            if board[i][jj] == 'B':
                break
            if board[i][jj] == 'p':
                out += 1
                break
        

        return out
