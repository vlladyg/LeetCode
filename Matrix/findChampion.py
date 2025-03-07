class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        winner = 0

        for i in range(1, len(grid)):
            if grid[winner][i] == 0:
                winner = i

        return winner
