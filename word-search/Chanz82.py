class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(current, word_idx):
            x, y = current

            if word_idx == len(word):
                return True

            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]): 
                return False

            if board[x][y] != word[word_idx] :
                return False
            
            tmp = board[x][y]
            board[x][y] = '#'

            found = (dfs((x-1, y), word_idx+1) or
                     dfs((x+1, y), word_idx+1) or
                     dfs((x, y-1), word_idx+1) or
                     dfs((x, y+1), word_idx+1))

            board[x][y] = tmp

            return found

        for x, rows in enumerate(board):
            for y, cell in enumerate(rows):
                if dfs((x, y), 0) == True : 
                    return True
        return False
