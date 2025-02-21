class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid_dict = {}
        self.grid = grid

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.grid_dict[grid[i][j]] = (i, j)



    def adjacentSum(self, value: int) -> int:
        res = 0
        n = len(self.grid)

        i, j = self.grid_dict[value]

        if i + 1 < n:
            res += self.grid[i + 1][j]
        if i - 1 >= 0:
            res += self.grid[i - 1][j]
        
        if j - 1 >= 0:
            res += self.grid[i][j - 1]

        if j + 1 < n:
            res += self.grid[i][j + 1]
        
        

        return res

    def diagonalSum(self, value: int) -> int:
        res = 0
        n = len(self.grid)

        i, j = self.grid_dict[value]
        
        if i + 1 < n and j - 1 >= 0:
            res += self.grid[i+1][j - 1]

        if i - 1 >= 0 and j + 1 < n:
            res += self.grid[i - 1][j + 1]
        
        if i - 1 >= 0 and j - 1 >= 0:
            res += self.grid[i - 1][j - 1]

        if i + 1 < n and j + 1 < n:
            res += self.grid[i + 1][j + 1]


        return res
