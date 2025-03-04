class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            if grid[i][i] == 0 or grid[i][n - i - 1] == 0:
                return False

        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0 and j != i and j != n - i - 1:
                    return False

        return True
