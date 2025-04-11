from collections import Counter

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # Initializing a counter to keep track of the frequency of each standardized row
        row_counter = Counter()
      
        # Iterating through each row in the matrix
        for row in matrix:
            # Standardizing the row:
            # If the first element is 0, keep the row unchanged; otherwise flip all bits
            standardized_row = tuple(row) if row[0] == 0 else tuple(1 - x for x in row)
          
            # Updating the counter for the standardized row
            row_counter[standardized_row] += 1
      
        # Returning the maximum frequency found in the counter as the result
        return max(row_counter.values())
