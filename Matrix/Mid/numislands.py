class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                diractions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in diractions:
                    rr, cc = row + dr, col + dc
                    if rr >= 0 and rr < rows and cc >= 0 and cc < cols and grid[rr][cc] == "1" and (rr, cc) not in visited:
                        q.append((rr, cc))
                        visited.add((rr, cc))
                        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands
