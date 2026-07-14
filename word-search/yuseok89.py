# TC: O(NML)
# SC: O(1)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n = len(board)
        m = len(board[0])

        def rec(row, col, idx):
            if idx == len(word):
                return True

            if row < 0 or row >= n or col < 0 or col >= m or board[row][col] != word[idx]:
                return False

            board[row][col] = None

            ret = rec(row + 1, col, idx + 1) or rec(row - 1, col, idx + 1) or rec(row, col + 1, idx + 1) or rec(row, col - 1, idx + 1)

            board[row][col] = word[idx]

            return ret

        for row in range(0, n):
            for col in range(0, m):
                if board[row][col] == word[0] and rec(row, col, 0):
                    return True

        return False

