class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def dfs(r, c):
            if min(r, c) < 0 or r == n or c == m or grid[r][c] == 0:
                return 0

            tmp = grid[r][c]
            grid[r][c] = 0
            res = 0
            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

            for rr, cc in neighbors:
                res = max(res, tmp + dfs(rr, cc))

            grid[r][c] = tmp
            return res

        res = 0
        for r in range(n):
            for c in range(m):
                res = max(res, dfs(r, c))
        return res
