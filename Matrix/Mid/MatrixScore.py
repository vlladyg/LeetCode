class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # Get the number of rows (m) and columns (n) in the grid
        num_rows, num_cols = len(grid), len(grid[0])

        # Flip the rows where the first element is 0
        for i in range(num_rows):
            if grid[i][0] == 0:
                for j in range(num_cols):
                    # XOR operation to flip the bits (0 becomes 1, and 1 becomes 0)
                    grid[i][j] ^= 1

        # Initialize the variable to store the result
        result = 0

        # Iterate over columns
        for j in range(num_cols):
            # Count the number of 1s in the current column
            num_ones = sum(grid[i][j] for i in range(num_rows))
            # Maximize the column value by flipping if necessary (the majority should be 1s)
            # Use the maximum of the number of 1s or the number of 0s in the column
            max_value = max(num_ones, num_rows - num_ones)
          
            # Add the value of the column to the result
            # The value is determined by the number of 1s times the value of the bit
            # position (1 << (num_cols - j - 1)) is the bit value of the current column
            result += max_value * (1 << (num_cols - j - 1))
      
        # Return the maximized score after considering all rows and columns
        return result
