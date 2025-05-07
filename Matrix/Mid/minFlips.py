class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        

        def calc(grid):
            n = len(grid)
            m = len(grid[0])

            count = 0
            for r in range(n):
                for c in range(m//2):
                    if grid[r][c] != grid[r][m - c - 1]:
                        count += 1


            return count


        gt = list(map(list, zip(*grid)))

        return min(calc(gt), calc(grid))
