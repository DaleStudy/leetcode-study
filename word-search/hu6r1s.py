class Solution:
    """
    1. dfs 방식
    dx = [1, -1, 0, 0], dy = [0, 0, 1, -1], visited = [[False] * m for _ in range(n)]
    4방향으로 가면서 해당 요소에 단어가 없으면 false
    방문한 적이 없어야 하고, 
    
    시간복잡도: O(N * L * 4^L)
    - N: 보드 크기 (n*m)
    - L: 단어 길이
    - 모든 좌표에서 DFS 시작 (N회) × 4방향 분기 (4^L) × 슬라이싱 비용 (O(L))
    공간복잡도: O(N + L^2)
    - visited 배열 O(N)
    - 재귀 호출 스택 O(L)
    - 문자열 슬라이싱으로 인한 추가 메모리 O(L^2)

    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        visited = [[False] * m for _ in range(n)]
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

        def dfs(x, y, w):
            if not w:
                return True
            if x < 0 or y < 0 or x >= n or y >= m:
                return False
            if visited[x][y] or board[x][y] != w[0]:
                return False
            
            visited[x][y] = True

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if dfs(nx, ny, w[1:]):
                    return True

            visited[x][y] = False
            return False

        for i in range(n):
            for j in range(m):
                if dfs(i, j, word):
                    return True
        return False
