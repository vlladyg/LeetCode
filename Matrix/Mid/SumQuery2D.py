class NumMatrix:
    def __init__(self, matrix):
        # First check if the matrix is empty to prevent IndexError
        if not matrix or not matrix[0]:
            raise ValueError("Matrix should not be empty")
      
        # Get the dimensions of the matrix
        self.num_rows, self.num_cols = len(matrix), len(matrix[0])
      
        # Create a 2D prefix sum array with an extra row and column (for easy calculation)
        self.prefix_sum = [[0] * (self.num_cols + 1) for _ in range(self.num_rows + 1)]
      
        # Calculate cumulative sum for the matrix and store it in prefix_sum array
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.prefix_sum[row + 1][col + 1] = (
                    self.prefix_sum[row][col + 1] +        # current row prefix sum
                    self.prefix_sum[row + 1][col] -        # current column prefix sum
                    self.prefix_sum[row][col] +            # subtract overlapping area
                    matrix[row][col]                       # add current matrix value
                )

    def sumRegion(self, row1, col1, row2, col2):
        # Retrieve the sum of the desired region using the inclusion-exclusion principle
        return (
            self.prefix_sum[row2 + 1][col2 + 1] -        # sum of entire rectangle from (0,0) to (row2, col2)
            self.prefix_sum[row2 + 1][col1] -            # subtract sum above the intended row range
            self.prefix_sum[row1][col2 + 1] +            # subtract sum before the intended column range
            self.prefix_sum[row1][col1]                  # add back the sum of the overlapping rectangle
        )                                                # that was subtracted twice


