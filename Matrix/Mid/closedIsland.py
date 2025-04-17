class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        visit = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r == n or c == m):
                return 0
            
            if grid[r][c] or (r, c) in visit:
                return 1

            visit.add((r, c))
            
            #if dfs(r + 1, c) and dfs(r - 1, c) and dfs(r, c + 1) and dfs(r, c - 1):
            #    return 1
            #else:
            #    return 0
            
            return min(dfs(r + 1, c), dfs(r - 1, c), dfs(r, c + 1), dfs(r, c - 1))



        res = 0

        for r in range(n):
            for c in range(m):
                if not grid[r][c] and (r, c) not in visit:
                    res += dfs(r, c)

        return res
