"""
Spiral traversal of a matrix: visit all elements in "spiral order" (clockwise from top-left).

Time Complexity: O(N), where N is the total number of elements in matrix.
    - Each element is visited once.

Space Complexity: O(N)
    - The output array includes all N elements.
    - The input matrix is modified in-place to mark visited cells.
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROW = len(matrix)
        COL = len(matrix[0])
        TARGET = ROW * COL
        DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        CHECK = -1000

        ans = []

        def bound(r: int, c: int) -> bool:
            return 0 <= r < ROW and 0 <= c < COL

        r = c = d = 0

        for _ in range(TARGET):
            ans.append(matrix[r][c])
            matrix[r][c] = CHECK

            tr = r + DIR[d][0]
            tc = c + DIR[d][1]
            if not bound(tr, tc) or matrix[tr][tc] == CHECK:
                d = (d + 1) % 4
            r += DIR[d][0]
            c += DIR[d][1]


        return ans
