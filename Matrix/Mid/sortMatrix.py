class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])

        s = collections.defaultdict(list)

        for r in range(n):
            for c in range(m):
                s[r - c].append(grid[r][c])

        for k in s.keys():
            s[k] = collections.deque(sorted(s[k]))

        for r in range(n):
            for c in range(m):
                if r - c >= 0:
                    grid[r][c] = s[r - c].pop()
                else:
                    grid[r][c] = s[r - c].popleft()


        return grid
