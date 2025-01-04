'''
# 79. Word Search

use backtracking(DFS) to search for the word in the board.

## Time and Space Complexity

```
TC: O(n * m * 4^L)
SC: O(L)
```

#### TC is O(n * m * 4^L):
- n is the number of rows in the board.
- m is the number of columns in the board.
- L is the length of the word.
  - 4^L is the number of directions we can go at each step. (explores 4 branches recursively)

#### SC is O(L):
- modifying the board in-place to mark visited cells. = O(L)
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        def backtracking(i, j, word_index): # TC: O(4^L), SC: O(L)
            if word_index == len(word):
                return True
            
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[word_index]:
                return False
            
            temp = board[i][j]
            board[i][j] = "."
            
            found = (
                backtracking(i + 1, j, word_index + 1) or
                backtracking(i - 1, j, word_index + 1) or
                backtracking(i, j + 1, word_index + 1) or
                backtracking(i, j - 1, word_index + 1)
            )
            board[i][j] = temp
            
            return found
        
        for row in range(rows): # TC: O(n * m)
            for col in range(cols):
                if backtracking(row, col, 0):
                    return True
                    
        return False
