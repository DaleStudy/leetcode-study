# TC : O(N * 4^L), where N is the number of cells in the board and L is the length of the word.
# SC : O(L) due to the recursive calls in the backtrack function, where L is the length of the word.
class Solution:
    def exist(self, board, word):
        def backtrack(i, j, k):
            # If we have checked all characters in the word
            if k == len(word):
                return True
            # If out of bounds or current cell does not match the word character
            if (
                i < 0
                or i >= len(board)
                or j < 0
                or j >= len(board[0])
                or board[i][j] != word[k]
            ):
                return False

            # Temporarily mark the cell as visited
            temp = board[i][j]
            board[i][j] = ""

            # Explore all possible directions: down, up, right, left
            found = (
                backtrack(i + 1, j, k + 1)
                or backtrack(i - 1, j, k + 1)
                or backtrack(i, j + 1, k + 1)
                or backtrack(i, j - 1, k + 1)
            )

            # Restore the original value of the cell
            board[i][j] = temp
            return found

        # Start from each cell in the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False
