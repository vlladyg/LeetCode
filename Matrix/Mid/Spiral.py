class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        out = []
        i = 0
        j = 0

        UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
        dir = RIGHT

        UP_WALL = 0
        RIGHT_WALL = m
        DOWN_WALL = n
        LEFT_WALL = -1

        while len(out) !=  m*n:
            if dir == RIGHT:
                while j < RIGHT_WALL:
                    out.append(matrix[i][j])
                    j += 1
                i, j = i + 1, j - 1
                RIGHT_WALL -= 1

            if dir == DOWN:
                while i < DOWN_WALL:
                    out.append(matrix[i][j])
                    i += 1
                i, j = i - 1, j - 1
                DOWN_WALL -= 1

            if dir == LEFT:
                while j > LEFT_WALL:
                    out.append(matrix[i][j])
                    j -= 1
                i, j = i - 1, j + 1
                LEFT_WALL += 1

            if dir == UP:
                while i > UP_WALL:
                    out.append(matrix[i][j])
                    i -= 1
                i, j = i + 1, j + 1
                UP_WALL += 1

            dir = (dir + 1) % 4

        return out
