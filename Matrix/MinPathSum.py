class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        min_path = [[0]*n for _ in range(m)]
        visited = [[False]*n for _ in range(m)]

        min_path[0][0] = grid[0][0]
        visited[0][0] = True
        for i in range(1, m):
            min_path[i][0] = min_path[i-1][0] + grid[i][0]
        

        for j in range(1, n):
           min_path[0][j] = min_path[0][j - 1] + grid[0][j]


        for i in range(1, m):
            for j in range(1, n):
                min_path[i][j] = grid[i][j] + min(min_path[i - 1][j], min_path[i][j - 1]) 
        
        return min_path[-1][-1]

