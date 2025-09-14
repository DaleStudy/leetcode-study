"""
https://leetcode.com/problems/set-matrix-zeroes/description/

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

TC: O(m * n)
SC: O(m + n), set 자료구조 사용
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        zero_rows = set() # 최대 m개의 행 인덱스 저장
        zero_cols = set() # 최대 n개의 열 인덱스 저장

        # 0이 있는 위치 찾기
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # 0이 있는 행과 열 모두 0으로 만들기
        for i in range(rows):
            for j in range(cols):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0
