class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        out = [[0]*n for _ in range(n)]
        i = 0
        j = 0

        UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
        dir = RIGHT

        UP_WALL = 0
        RIGHT_WALL = n
        DOWN_WALL = n
        LEFT_WALL = -1

        counter = 0
        while counter !=  n*n:
            if dir == RIGHT:
                while j < RIGHT_WALL:
                    counter += 1
                    out[i][j] = counter
                    j += 1
                i, j = i + 1, j - 1
                RIGHT_WALL -= 1

            if dir == DOWN:
                while i < DOWN_WALL:
                    counter += 1
                    out[i][j] = counter
                    i += 1
                i, j = i - 1, j - 1
                DOWN_WALL -= 1

            if dir == LEFT:
                while j > LEFT_WALL:
                    counter += 1
                    out[i][j] = counter
                    j -= 1
                i, j = i - 1, j + 1
                LEFT_WALL += 1

            if dir == UP:
                while i > UP_WALL:
                    counter += 1
                    out[i][j] = counter
                    i -= 1
                i, j = i + 1, j + 1
                UP_WALL += 1

            dir = (dir + 1) % 4

        return out
