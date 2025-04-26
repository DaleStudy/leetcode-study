"""
시간 복잡도: O(N * M * 4^(word_len))
공간 복잡도: O(word_len) 재귀 스택 최대 깊이 word_len
"""
from collections import deque

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        word_len = len(word)

        def dfs(x: int, y: int, idx: int) -> bool:
            if idx == word_len:
                return True
            if x < 0 or y < 0 or x >= m or y >= n:
                return False
            if board[y][x] != word[idx]:
                return False
            
            tmp, board[y][x] = board[y][x], '#'
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if dfs(x + dx, y + dy, idx + 1):
                    return True

            board[y][x] = tmp
            return False
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and dfs(j, i, 0):
                    return True
        
        return False
