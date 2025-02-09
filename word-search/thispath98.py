class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Intuition:
            보드를 돌면서 dfs를 수행한다.
            dfs는 상하좌우를 돌면서 word의 index와
            board의 word가 동일한지 확인한다.

        Time Complexity:
            O(M x N + w.length^4):
                M x N 크기의 배열을 돌면서,
                각 칸마다 상하좌우 4번씩 확인한다.
                최대 word length번만큼 반복한다.

        Space Complexity:
            O(M x N + w.length):
                M x N 크기의 visited 배열을 초기화하고,
                dfs의 호출 스택은 word length만큼 반복한다.
        """
        visited = [[False for _ in board[0]] for _ in board]

        def dfs(y, x, index):
            if index == len(word):
                return True
            if not (0 <= y < len(board) and 0 <= x < len(board[0])):
                return False
            if visited[y][x]:
                return False
            if word[index] != board[y][x]:
                return False

            visited[y][x] = True
            for dy, dx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                ny = y + dy
                nx = x + dx

                if dfs(ny, nx, index + 1):
                    return True

            visited[y][x] = False
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        return False
