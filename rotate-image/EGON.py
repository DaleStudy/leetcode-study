from typing import List
from unittest import TestCase, main


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        return self.solve(matrix)

    """
    Runtime: 0 ms (Beats 100.00%)
    Time Complexity: O(n ^ 2)
        - 행렬의 행과 열을 교환하기 위해 이중 for문 사용에 O(n ^ 2)
        - 행렬의 각 행을 뒤집기 위해, 행을 조회하는데 O(n)
            - 각 행을 뒤집는데 * O(n)
        > O(n ^ 2) + O(n) * O(n) ~= O(n ^ 2) + O(n ^ 2) ~= O(n ^ 2) 

    Memory: 16.76 MB (Beats 14.84%)
    Space Complexity: O(1)
        > in-place 풀이이므로 상수 변수 할당을 제외한 메모리 사용 없음, O(1)
    """
    def solve(self, matrix: List[List[int]]) -> None:
        N = len(matrix)

        for i in range(N):
            for j in range(i, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        output = [[7,4,1],[8,5,2],[9,6,3]]
        Solution().rotate(matrix)
        self.assertEqual(matrix, output)

    def test_2(self):
        matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        output = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        Solution().rotate(matrix)
        self.assertEqual(matrix, output)


if __name__ == '__main__':
    main()
