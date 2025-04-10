class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x = 0
        o = 0

        def count(c):
            count = 0
            for i in range(3):
                for j in range(3):
                    if board[i][j] == c:
                        count += 1

            return count

        def win(c):
            for i in range(3):
                if all(board[i][j] == c for j in range(3)):
                    return True

            for i in range(3):
                if all(board[j][i] == c for j in range(3)):
                    return True

            if all(board[j][j] == c for j in range(3)):
                return True

            if all(board[3 - j - 1][j] == c for j in range(3)):
                return True

            return False

        x = count("X")
        o = count("O")

        if o > x or x > o + 1:
            return False

        xwin = win("X")
        owin = win("O")

        if xwin and owin:
            return False

        if xwin:
            if x != o + 1:
                return False
        
        if owin:
            if x != o:
                return False
        
        return True
