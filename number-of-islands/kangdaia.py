class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """1이 땅이고, 0이 바다로 표현한 2D리스트에서 연결되지 않은 땅 (섬)의 갯수를 구하는 함수

        방법:
        1. deque를 사용해 BFS로 풀이
            - 1이 땅인 경우, 섬 갯수 +1, 그리고 해당 땅과 연결된 땅을 모두 0으로 바꿔주며 탐색
        2. deque 대신 stack을 사용해 DFS로 풀이
        시간 복잡도: O(m*n) - 모든 땅을 탐색하는 경우
        공간 복잡도: O(m*n) - 최악의 경우 모든 땅이 연결되어 있는 경우

        Args:
            grid (list[list[str]]): 1과 0으로 구성된 2d array 지도

        Returns:
            int: 총 땅 갯수
        """
        
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        islands = 0

        for x in range(m):
            for y in range(n):
                if grid[x][y] != "1":
                    continue
                islands += 1
                stack = [(x, y)]
                grid[x][y] = "0"
                while stack:
                    i_x, i_y = stack.pop()
                    for dx, dy in directions:
                        nx, ny = i_x + dx, i_y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                            grid[nx][ny] = "0"
                            stack.append((nx, ny))
        return islands
