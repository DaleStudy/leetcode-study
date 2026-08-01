# TC: R is the number of rows, C is the number of columns.
#   spiralOrder: O(R * C) - visits every cell in the matrix exactly once

# SC:
#   spiralOrder: O(1) - auxiliary space excluding the output array

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []

        dir = 0 
        row = 0
        col = 0

        n = len(matrix)
        m = len(matrix[0])
        size = n * m

        VISIT = -200
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]

        while len(answer) < size:
            item = matrix[row][col]
            answer.append(item)

            next_row = row + dr[dir]
            next_col = col + dc[dir]

            if (
                next_row < 0
                or next_row >= n
                or next_col < 0
                or next_col >= m
                or matrix[next_row][next_col] == VISIT
            ):
                dir = (dir + 1) % 4

            matrix[row][col] = VISIT

            row += dr[dir]
            col += dc[dir]

        return answer
