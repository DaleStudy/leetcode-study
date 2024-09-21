from typing import List
from unittest import TestCase, main


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return self.solve(matrix)

    """
    Runtime: 37 ms (Beats 44.53%)
    Time Complexity: O(MAX_R * MAX_C)

    Memory: 16.56 MB (Beats 43.42%)
    Space Complexity: O(1)
        - result를 제외하고 matrix의 값을 변경해서 visited 분기
    """
    def solve(self, matrix: List[List[int]]) -> List[int]:
        MAX_R, MAX_C = len(matrix), len(matrix[0])
        DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        result = []
        r, c, dir_idx = 0, -1, 0
        for _ in range(MAX_R * MAX_C):
            r += DIRS[dir_idx][0]
            c += DIRS[dir_idx][1]

            if 0 <= r < MAX_R and 0 <= c < MAX_C and matrix[r][c] is not None:
                result.append(matrix[r][c])
                matrix[r][c] = None
            else:
                r -= DIRS[dir_idx][0]
                c -= DIRS[dir_idx][1]
                dir_idx = (dir_idx + 1) % len(DIRS)
                r += DIRS[dir_idx][0]
                c += DIRS[dir_idx][1]
                result.append(matrix[r][c])
                matrix[r][c] = None

        return result


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        output = [1,2,3,4,8,12,11,10,9,5,6,7]
        self.assertEqual(Solution.spiralOrder(Solution(), matrix), output)


if __name__ == '__main__':
    main()
