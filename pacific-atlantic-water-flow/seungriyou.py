# https://leetcode.com/problems/pacific-atlantic-water-flow/

from typing import List

class Solution:
    def pacificAtlantic_bfs(self, heights: List[List[int]]) -> List[List[int]]:
        """
        [Complexity]
            - TC: O(m * n) (모든 칸은 최대 한 번씩 방문)
            - SC: O(m * n) (queue)

        [Approach]
            거꾸로 각 바다에 맞닿아있는 edges에서부터 시작해서, BFS로 height 값이 gte인 칸(-> 바다에서부터 거꾸로 확인하므로)을 방문하며 기록한다.
            pacific & atlantic 쪽 edges에서 시작해서 방문한 칸들의 교집합을 구하면 된다.
        """
        from collections import deque

        m, n = len(heights), len(heights[0])
        dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

        def bfs(start_cells):
            q = deque(start_cells)
            visited = set(start_cells)

            while q:
                r, c = q.popleft()

                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]

                    if (
                            0 <= nr < m and 0 <= nc < n  # valid한 범위 확인
                            and (nr, nc) not in visited  # 방문 여부 확인
                            and heights[nr][nc] >= heights[r][c]  # height 값이 현재 칸보다 gte인지 확인 (** 거꾸로 확인하므로)
                    ):
                        q.append((nr, nc))
                        visited.add((nr, nc))

            return visited

        # pacific & atlantic 쪽 edges 모으기
        edges_p, edges_a = [], []
        for r in range(m):
            edges_p.append((r, 0))
            edges_a.append((r, n - 1))
        for c in range(n):
            edges_p.append((0, c))
            edges_a.append((m - 1, c))

        # edges로부터 BFS로 방문
        visited_p = bfs(edges_p)
        visited_a = bfs(edges_a)

        # pacific과 atlantic의 교집합 반환
        return [list(cell) for cell in visited_p & visited_a]

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        [Complexity]
            - TC: O(m * n) (모든 칸은 최대 한 번씩 방문)
            - SC: O(m * n) (call stack)

        [Approach]
            BFS 풀이를 DFS로도 접근 가능하다.
        """
        m, n = len(heights), len(heights[0])
        dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
        visited_p, visited_a = set(), set()

        def dfs(r, c, visited):
            # base condition
            if (r, c) in visited:  # 방문 여부 확인
                return

            # 방문 처리
            visited.add((r, c))

            # recur
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                if (
                        0 <= nr < m and 0 <= nc < n  # valid한 범위 확인
                        and heights[nr][nc] >= heights[r][c]  # height 값이 현재 칸보다 gte인지 확인 (** 거꾸로 확인하므로)
                ):
                    dfs(nr, nc, visited)

        # edges로부터 DFS로 방문
        for r in range(m):
            dfs(r, 0, visited_p)
            dfs(r, n - 1, visited_a)
        for c in range(n):
            dfs(0, c, visited_p)
            dfs(m - 1, c, visited_a)

        # pacific과 atlantic의 교집합 반환
        return [list(cell) for cell in visited_p & visited_a]
