from typing import List
from unittest import TestCase, main
from math import isnan


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        return self.solve(matrix)

    """
    Runtime: 107 ms (Beats 31.81%)
    Time Complexity:
        - matrix의 원소에 R_MARKER, C_MARKER를 더하는데 range(m), range(n) 조회에 O(m * n)
        - MARKER가 아닌 matrix의 원소를 0으로 바꾸는데 O(m * n)
        - MARKER인 matrix의 원소를 0으로 바꾸는데 O(m + n)
        > O(m * n) + O(m * n) + O(m + n) = O(2 * m * n) + O(m + n) ~= O(m * n) + O(m + n)
    Memory: 17.49 (Beats 58.33%)
    Space Complexity: O(1)
        > matrix의 원소의 값만 변경한 in-place 풀이이므로 O(1)
    """
    def solve(self, matrix: List[List[int]]) -> None:
        MAX_R, MAX_C = len(matrix), len(matrix[0])
        R_MARKER, C_MARKER, CROSS_MARKER = float('inf'), float('-inf'), float('nan')

        for r in range(MAX_R):
            for c in range(MAX_C):
                if matrix[r][c] == 0:
                    matrix[r][0] += R_MARKER
                    matrix[0][c] += C_MARKER

        for r in range(MAX_R):
            for c in range(MAX_C):
                if isnan(matrix[r][c]) or (matrix[r][c] in (R_MARKER, C_MARKER)):
                    continue

                if isnan(matrix[r][0]) or matrix[r][0] == R_MARKER:
                    matrix[r][c] = 0

                if isnan(matrix[0][c]) or matrix[0][c] == C_MARKER:
                    matrix[r][c] = 0

        for r in range(MAX_R):
            if isnan(matrix[r][0]) or matrix[r][0] == R_MARKER:
                matrix[r][0] = 0
        for c in range(MAX_C):
            if isnan(matrix[0][c]) or matrix[0][c] == C_MARKER:
                matrix[0][c] = 0


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        output = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
        Solution.setZeroes(Solution(), matrix)
        self.assertEqual(matrix, output)

    def test_2(self):
        matrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
        output = [[0,0,3,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        Solution.setZeroes(Solution(), matrix)
        self.assertEqual(matrix, output)


if __name__ == '__main__':
    main()
