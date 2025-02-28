class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[0]*(n-2) for _ in range(n - 2)]
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                maxLocal[i-1][j-1] = max(grid[i][j], grid[i+1][j+1], grid[i-1][j-1], grid[i-1][j], grid[i][j-1], grid[i][j+1], grid[i+1][j], grid[i+1][j-1], grid[i-1][j+1])

        return maxLocal
