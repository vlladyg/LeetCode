class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        def one_step(i, j):
            counter = (grid[i][j] == 'W') + (grid[i+1][j]  == 'W') + (grid[i][j+1]  == 'W') + (grid[i+1][j+1]  == 'W')
            if counter > 2 or counter < 2:
                return True

            return False

        if one_step(0, 0) or one_step(0, 1) or one_step(1, 0) or one_step(1, 1):
            return True

        return False
