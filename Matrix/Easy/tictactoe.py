class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[' ']*3 for _ in range(3)]
        for i, el in enumerate(moves):
            if i % 2 == 0:
                grid[el[0]][el[1]] = 'X'

                if grid[0][0] == grid[1][1] == grid[2][2] == 'X' or grid[2][0] == grid[1][1] == grid[0][2] == 'X':
                    return 'A'

                if grid[0][el[1]] == grid[1][el[1]] == grid[2][el[1]] == 'X' or grid[el[0]][0] == grid[el[0]][1] == grid[el[0]][2] == 'X':
                    return 'A'

            else:
                grid[el[0]][el[1]] = 'O'

                if grid[0][0] == grid[1][1] == grid[2][2] == 'O' or grid[2][0] == grid[1][1] == grid[0][2] == 'O':
                    return 'B'

                if grid[0][el[1]] == grid[1][el[1]] == grid[2][el[1]] == 'O' or grid[el[0]][0] == grid[el[0]][1] == grid[el[0]][2] == 'O':
                    return 'B'
            


        if len(moves) == 9:
            return 'Draw'
        else:
            return 'Pending'
