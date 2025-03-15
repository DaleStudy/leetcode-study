# Time Complexity: O(m * n * 4^l) -> each cell can explore up to 4 directions recursively, where l is the max word length.
# Space Complexity: O(w * l) -> storing words in a dictionary-based Trie.

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:    
        # trie-like dictionary to store words    
        d = {} 
        
        # build the trie
        for word in words:
            cur = d
            for c in word:
                if c not in cur:
                     # create a new node
                    cur[c] = {} 
                cur = cur[c]
            # mark the end of the word
            cur["*"] = word  
        
        # right, down, up, left
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  
        
        # backtracking function
        def dfs(i, j, cur, seen):
            result = set()
            if "*" in cur:
                # found a word, add it
                result = {cur["*"]}  
            
            for x, y in directions:
                ni, nj = i + x, j + y
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and (ni, nj) not in seen and board[ni][nj] in cur:
                    result.update(dfs(ni, nj, cur[board[ni][nj]], seen | {(ni, nj)}))
            
            return result
        
        result = set()
        
        # start dfs search from every cell in the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in d:
                    result.update(dfs(i, j, d[board[i][j]], {(i, j)}))
        
        return list(result)  
