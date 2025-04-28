# https://leetcode.com/problems/word-search/

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        [Complexity]
            - TC: O(m * n * 4^L) (L = word의 길이)
                - 한 경로에서 최대 L번 재귀 호출
                - 각 cell 당 3~4 방향 가능
            - SC: O(m * n + L) (visited + call stack)
                - visited 배열 대신 board에 inplace로 표시하면 O(L)으로 최적화 가능

        [Approach]
            주어진 word를 순차적으로 확인하기 위해 backtracking으로 접근할 수 있다. (가지치기 가능)
            맨 처음에 word를 구성하는 문자가 board에 모두 존재하는지 확인한다면 run time을 줄일 수 있다.
        """
        # early stop (word를 구성하는 문자가 board에 모두 존재하는지 확인)
        if set(word) - set(l for row in board for l in row):
            return False

        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        def backtrack(r, c, idx):
            # base condition
            if idx == len(word):
                return True
            if (
                    not (0 <= r < m and 0 <= c < n)  # (1) 범위를 벗어나거나
                    or visited[r][c]  # (2) 이미 방문했거나
                    or board[r][c] != word[idx]  # (3) 주어진 word와 다른 경우
            ):
                return False

            # backtrack
            visited[r][c] = True
            if (
                    backtrack(r - 1, c, idx + 1)
                    or backtrack(r + 1, c, idx + 1)
                    or backtrack(r, c - 1, idx + 1)
                    or backtrack(r, c + 1, idx + 1)
            ):
                return True
            visited[r][c] = False

            return False

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True

        return False
