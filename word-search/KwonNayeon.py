"""
Constraints:
 1. m equals board length (number of rows)
 2. n equals board[i] length (number of columns)
 3. m and n are between 1 and 6 inclusive
 4. word length is between 1 and 15 inclusive
 5. board and word contain only lowercase and uppercase English letters

Time Complexity: O(N * 4^L)
 - N은 board의 모든 cell (m * n)
 - L은 word의 길이
 - 각 cell에서 시작하여 word의 각 글자마다 네방향으로 탐색 (이미 방문한 방향 제외)

Space Complexity: O(L)
 - L은 word의 길이로, 재귀 호출 스택의 깊이
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(i, j, k):

            # 단어를 모두 찾았으면 True 반환
            if k == len(word):
                return True
            
            if (i < 0 or i >= rows or       # 경계체크
                j < 0 or j >= cols or 
                board[i][j] != word[k]):    # 현재 문자가 찾는 문자와 다름
                return False
            
            temp = board[i][j]      # 현재 문자를 임시저장
            board[i][j] = '#'       # 방문 표시
            
            result = (dfs(i+1, j, k+1) or   # 상하좌우 네 방향 탐색
                     dfs(i-1, j, k+1) or 
                     dfs(i, j+1, k+1) or 
                     dfs(i, j-1, k+1))
            
            board[i][j] = temp      # 백트래킹 (원래 문자로 복원)
            return result
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False
