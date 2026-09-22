VISITED = '#'

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = 0
        col = 0

        visit = []

        def canGo(row, col):
            if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
                return False

            if matrix[row][col] == VISITED:
                return False

            return True

        while True:
            if not (canGo(row, col + 1) or canGo(row + 1, col) or canGo(row, col - 1) or canGo(row - 1, col)):
                break

            while canGo(row, col + 1):
                visit.append(matrix[row][col])

                matrix[row][col] = VISITED
                col += 1

            while canGo(row + 1, col):
                visit.append(matrix[row][col])

                matrix[row][col] = VISITED
                row += 1

            while canGo(row, col - 1):
                visit.append(matrix[row][col])

                matrix[row][col] = VISITED
                col -= 1

            while canGo(row - 1, col):
                visit.append(matrix[row][col])

                matrix[row][col] = VISITED
                row -= 1

        visit.append(matrix[row][col])

        return visit
