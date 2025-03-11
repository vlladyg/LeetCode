class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        final = [True]*n**2
        sum_el = (1+n*n)*n*n/2
        for i in range(n):
            for j in range(n):
                if final[grid[i][j]-1] == True:
                    final[grid[i][j]-1] = False
                    sum_el -= grid[i][j]
                else:
                    a = grid[i][j]

        return a, int(sum_el)
