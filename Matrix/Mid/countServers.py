class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        row_cnt = [0] * n
        col_cnt = [0] * m

        # Preprocessing
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    row_cnt[r] += 1
                    col_cnt[c] += 1

        res = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] and ( row_cnt[r] > 1 or col_cnt[c] > 1 ):
                    res += 1

        
        return res
