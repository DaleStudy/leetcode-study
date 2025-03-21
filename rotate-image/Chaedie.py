"""
Solution: 1) 가장 바깥에서부터 안쪽으로 들어오며 4 원소의 자리를 바꿔준다.
Time: O(n^2)
Space: O(1)
"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])


        l, r = 0, COLS - 1
        t, b = 0, ROWS - 1
        while l < r and t < b:
            for i in range(r - l):
                [
                    matrix[t][l + i], 
                    matrix[t + i][r], 
                    matrix[b][r - i], 
                    matrix[b - i][l]
                ] = [
                    matrix[b - i][l], 
                    matrix[t][l + i], 
                    matrix[t + i][r],
                    matrix[b][r - i]
                ]

            l += 1
            r -= 1
            t += 1
            b -= 1
