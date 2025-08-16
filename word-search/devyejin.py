class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def backtrack(x, y, idx):
            if idx == len(word):
                return True

            if not (0 <= x < m and 0 <= y < n) or board[x][y] != word[idx]:
                return False

            tmp, board[x][y] = board[x][y], "@"

            res = (
                    backtrack(x + 1, y, idx + 1) or
                    backtrack(x - 1, y, idx + 1) or
                    backtrack(x, y + 1, idx + 1) or
                    backtrack(x, y - 1, idx + 1)
            )

            board[x][y] = tmp
            return res

        m = len(board)
        n = len(board[0])

        for r in range(m):
            for c in range(n):
                if backtrack(r, c, 0):
                    return True

        return False
