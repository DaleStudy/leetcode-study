# DFS 풀이
# board 높이: m, 넓이: n, w: 단어의 길이
# TC: (m * n * 4^w) -> 4^w 상하좌우 탐색 * 글자판 내의 모든 좌표를 상대로 수행함
# SC: O(m * n + w) -> traversing 집합 메모리는 글자판의 크기의 비례 + dfs 호출 스택의 깊이가 단어의 길이에 비례해 증가

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n_rows, n_cols = len(board), len(board[0])
        traversing = set()

        def dfs(row, col, idx):
            if idx == len(word):
                return True
            if not (0 <= row < n_rows and 0 <= col < n_cols):
                return False
            if (row, col) in traversing:
                return False
            if board[row][col] != word[idx]:
                return False

            traversing.add((row, col))
            # 상하좌우 탐색
            for (r, c) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if dfs(row + r, col + c, idx + 1):
                    return True
            traversing.remove((row, col))
            return False

        for i in range(n_rows):
            for j in range(n_cols):
                if dfs(i, j, 0):
                    return True
        return False
