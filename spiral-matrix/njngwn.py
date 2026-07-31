class Solution:
    # Time Complexity: O(n*m), n: len(matrix), m: len(matrix[0])
    # Space Complexity: O(1)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # left, right, up, down
        left, right, top, bottom = 0, len(matrix[0])-1, 0, len(matrix)-1    # borders
        i, j, d = 0, 0, direction[1]

        while left <= right and top <= bottom and 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
            # change direction and borders
            if j == right and d == direction[1]:
                d = direction[3] # right -> down
                top += 1
            elif i == bottom and d == direction[3]:
                d = direction[0]  # down -> left
                right -= 1
            elif j == left and d == direction[0]:
                d = direction[2]  # left -> up
                bottom -= 1
            elif i == top and d == direction[2]:
                d = direction[1]  # up -> right
                left += 1

            # append val to the result
            result.append(matrix[i][j])
            i += d[0]
            j += d[1]

        return result
