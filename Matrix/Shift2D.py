class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])

        return [[ grid[(i + (j - k) // m) % n][(j - k) % m] for j in range(m)] for i in range(n)]
