"""
Blind 75 - Word Search
LeetCode Problem Link: https://leetcode.com/problems/word-search/
시간복잡도 : 
공간복잡도 :
풀이 : DFS + 백트래킹
1. 전체 순회하여 단어의 첫 글자와 일치하는 지점 찾기
2. 첫 글자 List에 대해서 DFS 수행하여 있다면 return True
3. 없다면 return False
visited를 별도로 저장하는 대신 board의 글자를 임시로 변경하여 방문처리(backtracking)
-> 잊지 말고 board[i][j] = char 로 원상복구 시키기
"""
from typing import List

class Solution:
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def dfs(self, board, word, i, j, word_index):
        # 종료 조건
        if word_index == len(word):
            return True
        
        # 실패 조건
        if (i < 0 or i >= len(board) or 
            j < 0 or j >= len(board[0]) or 
            board[i][j] != word[word_index]):
            return False
        char = board[i][j]
        board[i][j] = '#' 
        # 4방향 탐색
        for direction in range(4):
            ni = i + self.dx[direction]
            nj = j + self.dy[direction]
            if self.dfs(board, word, ni, nj, word_index + 1):
                board[i][j] = char
                return True
        board[i][j] = char
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        for i in range(rows):
            for j in range(cols):
                if self.dfs(board, word, i, j, 0):
                    return True
        return False