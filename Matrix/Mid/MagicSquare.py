        class Solution:
            def numMagicSquaresInside(self, grid: List[List[int]]) -> int:  
                n = len(grid)
                m = len(grid[0])
                ans = 0
            
                for i in range(0, n - 2): 
                    for j in range(0, m - 2): 
            
                        # if condition true skip check 
                        if grid[i + 1][j + 1] != 5: 
                            continue
            
                        # check for magic square subgrid  
                        ans += magic(grid[i][j], grid[i][j + 1], 
                            grid[i][j + 2], grid[i + 1][j], 
                            grid[i + 1][j + 1], grid[i + 1][j + 2], 
                            grid[i + 2][j], grid[i + 2][j + 1], 
                            grid[i + 2][j + 2])
            
                # return total magic square 
                return ans 

            # function to check is subgrid is Magic Square 
        def magic(a, b, c, d, e, f, g, h, i): 
        
            s1 = set([a, b, c, d, e, f, g, h, i]) 
            s2 = set([1, 2, 3, 4, 5, 6, 7, 8, 9]) 
        
            # Elements of grid must contain all numbers 
            # from 1 to 9, sum of all rows, columns and 
            # diagonals must be same, i.e., 15. 
            return (s1 == s2 and (a + b + c) == 15 and
            (d + e + f) == 15 and (g + h + i) == 15 and
            (a + d + g) == 15 and (b + e + h) == 15 and
            (c + f + i) == 15 and (a + e + i) == 15 and
            (c + e + g) == 15)
