class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        # Sort each row in ascending order
        for row in grid:
            row.sort()
        
        # Compute the sum of maximums from the last column to the first
        result = 0
        for col in zip(*grid):  # Unzip columns from sorted rows
            result += max(col)  # Add the maximum from this "deleted" column
        
        return result

