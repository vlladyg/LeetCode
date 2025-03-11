class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        counter = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if i == 0:
                        counter += 1
                    elif grid[i-1][j] == 0:
                            counter += 1

                    if i == n - 1:
                        counter += 1
                    elif grid[i+1][j] == 0:
                            counter += 1
                    
                    if j == 0:
                        counter += 1
                    elif grid[i][j - 1] == 0:
                            counter += 1

                    if j == m - 1:
                        counter += 1
                    elif grid[i][j + 1] == 0:
                            counter += 1

        return counter
