class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        m = len(grid[0])

        out = []
        

        if m % 2 == 1:
            for i in range(n):
                if i % 2 == 0:
                    out.extend(grid[i][::2])
                else:
                    out.extend(grid[i][::-1][1::2])
        else:
            for i in range(n):
                if i % 2 == 0:
                    out.extend(grid[i][::2])
                else:
                    out.extend(grid[i][::-1][::2])
        
        return out
