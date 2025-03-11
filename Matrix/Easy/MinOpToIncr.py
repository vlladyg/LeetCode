class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        output = 0
        for j in range(len(grid[0])):
            maxval = grid[0][j]
            for i in range(1, len(grid)):
                if grid[i][j] <= maxval:
                    output += maxval + 1 - grid[i][j]
                    maxval += 1
                else:
                    maxval = grid[i][j]
        return output
