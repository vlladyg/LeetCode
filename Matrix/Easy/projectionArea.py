class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        return sum([max(row) for row in grid]) + sum([max(col) for col in zip(*grid)]) + sum([1 for i in range(n) for j in range(m) if grid[i][j] > 0])
