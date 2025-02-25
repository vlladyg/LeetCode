class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_row = [min(row) for row in matrix]
        max_col = [max(col) for col in zip(*matrix)]
        
        return [row for row in min_row if row in max_col]
        
            
