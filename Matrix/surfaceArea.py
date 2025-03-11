class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        counter = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    counter += 2
                if i == 0:
                    counter += grid[i][j]
                elif grid[i][j] - grid[i-1][j] > 0:
                    counter += grid[i][j] - grid[i-1][j]
                if i == n - 1:
                    counter += grid[i][j]
                elif grid[i][j] - grid[i+1][j] > 0:
                    counter += grid[i][j] - grid[i+1][j]
                

                if j == 0:
                    counter += grid[i][j]
                elif grid[i][j] - grid[i][j-1] > 0:
                    counter += grid[i][j] - grid[i][j-1]
                if j == m - 1:
                    counter += grid[i][j]
                elif grid[i][j] - grid[i][j+1] > 0:
                    counter += grid[i][j] - grid[i][j+1]
                

        return counter
