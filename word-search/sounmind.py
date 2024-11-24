from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, k):
            if k == len(word):
                return True

            # out of range
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False

            # char not found
            if board[row][col] != word[k]:
                return False

            temp = board[row][col]

            # mark visited char
            board[row][col] = None

            result = (
                dfs(row + 1, col, k + 1)  # top
                or dfs(row - 1, col, k + 1)  # bottom
                or dfs(row, col + 1, k + 1)  # right
                or dfs(row, col - 1, k + 1)  # left
            )

            # restore char
            board[row][col] = temp

            return result

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0):
                    return True

        return False
