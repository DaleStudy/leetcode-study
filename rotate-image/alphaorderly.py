"""
시간복잡도: O(n^2)
공간복잡도: O(1)

- 행렬을 전치 행렬로 변환
- 각 행을 중간 열을 기준으로 뒤집음
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)

        for r in range(N):
            for c in range(r + 1, N):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for r in range(N):
            for c in range(N // 2):
                matrix[r][c], matrix[r][-c - 1] = matrix[r][-c - 1], matrix[r][c]
