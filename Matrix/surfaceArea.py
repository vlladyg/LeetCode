class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        counter = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    counter += 1
        counter *= 2

        row_sum = 0
        for i in range(n):
            tmp = grid[i][-1] + grid[i][0]

            for j in range(1, n):
                tmp += abs(grid[i][j-1] - grid[i][j])
            row_sum += tmp

        col_sum = 0
        for j in range(n):
            tmp = grid[-1][j] + grid[0][j]
            for i in range(1, n):
                tmp += abs(grid[i-1][j] - grid[i][j])
            col_sum += tmp

        return counter + col_sum + row_sum
