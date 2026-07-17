from collections import Counter
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_len, col_len = len(board), len(board[0])

        board_freq = Counter(ch for row in board for ch in row)

        if board_freq.get(word[0], 0) > board_freq.get(word[-1], 0):
            word = word[::-1]

        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        MARKER = ""

        def in_bounds(r: int, c: int) -> bool:
            return 0 <= r < row_len and 0 <= c < col_len

        def backtrack(r: int, c: int, idx: int) -> bool:
            for ch, need in Counter(word[idx:]).items():
                if board_freq.get(ch, 0) < need:
                    return False

            if idx == len(word) - 1:
                return True

            saved_char = board[r][c]
            board[r][c] = MARKER
            board_freq[saved_char] -= 1

            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                next_ch = word[idx + 1]

                if (in_bounds(nr, nc)
                        and board[nr][nc] != MARKER
                        and board[nr][nc] == next_ch
                        and board_freq[next_ch] > 0
                        and backtrack(nr, nc, idx + 1)):
                    return True

            board[r][c] = saved_char
            board_freq[saved_char] += 1
            return False

        for r in range(row_len):
            for c in range(col_len):
                if board[r][c] == word[0] and backtrack(r, c, 0):
                    return True

        return False
