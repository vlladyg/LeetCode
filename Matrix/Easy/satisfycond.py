class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if i + 1 < n and grid[i][j] != grid[i+1][j]:
                    return False

        for j in range(m):
            if j + 1 < m and grid[0][j] == grid[0][j + 1]:
                return False

        return True
