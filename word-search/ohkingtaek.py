class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        시간 복잡도: O(M * N * 4^L)
        공간 복잡도: O(M * N)
        1. 행렬을 순회하며 단어의 첫 번째 문자와 일치하는 위치를 찾기
        2. 찾은 위치에서 상하좌우로 이동하며 단어의 다음 문자와 일치하는 위치를 찾기
        3. 단어의 마지막 문자까지 찾으면 True를 반환, 못 찾으면 False
        """
        m, n = len(board), len(board[0])

        def dfs(i, j, k):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            t = board[i][j]
            board[i][j] = "#"
            dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
            ok = False
            for d in range(4):
                if dfs(i + dx[d], j + dy[d], k + 1):
                    ok = True
                    break
            board[i][j] = t
            return ok

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
