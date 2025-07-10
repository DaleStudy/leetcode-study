"""
LeetCode 48. Rotate Image
https://leetcode.com/problems/rotate-image/

summary:
n x n 행렬을 시계 방향으로 90도 회전(in-place, 추가 공간없이 행렬 자체를 수정)
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 시간복잡도 O(n^2), 공간복잡도 O(1) 

        n = len(matrix)
        
        # 행과 열 바꾸기
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 행을 좌우반전하기
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
