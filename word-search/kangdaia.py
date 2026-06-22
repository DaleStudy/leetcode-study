class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """m*n 사이즈 보드가 주어졌을 때, word를 만들 수 있는지 true/false로 return 하는 함수

        1. bfs로 queue에 모든 element를 추가하고, 매번 path를 파악해서 word인지 판단하도록 함
        -> 시간 효율이 안나옴
        2. dfs 방식 적용. 현재 탐색 중일때, 보드를 #으로 치환해서, 이미 방문한 곳임을 체크
            - 시작점이 word[0]와 같을 때만 시작
            - dfs는 전체 path를 기록하지 않고, word가 볼 index를 인자로 받도록 함.

        Args:
            board (list[list[str]]): 글자를 element로 가진 2d array
            word (str): 찾아야 할 글자 목록

        Returns:
            bool: word가 board에 있는지 여부
        """
        m, n = len(board[0]), len(board)

        def dfs(row, col, idx):
            if board[row][col] != word[idx]:
                return False
            if idx == len(word) - 1:
                return True
            visited = board[row][col]
            board[row][col] = "#"
            for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                if 0 <= r < n and 0 <= c < m:
                    if dfs(r, c, idx + 1):
                        board[row][col] = visited
                        return True
            board[row][col] = visited
            return False

        for ir in range(n):
            for ic in range(m):
                if board[ir][ic] == word[0] and dfs(ir, ic, 0):
                    return True
        return False
