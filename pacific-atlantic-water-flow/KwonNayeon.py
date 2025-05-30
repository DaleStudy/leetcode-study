"""
Constraints:
- m == heights.length
- n == heights[r].length
- 1 <= m, n <= 200
- 0 <= heights[r][c] <= 10^5

Time Complexity: O(m*n) 
- 각 셀을 최대 한 번만 방문함

Space Complexity: O(m*n)
- visited sets(pacific, atlantic)은 최대 m*n 크기
- 재귀 호출 스택도 최대 m*n까지 가능

풀이방법:
1. Pacific(좌측상단)과 Atlantic(우측하단)의 경계에서 시작
2. DFS로 현재 높이보다 높거나 같은 인접 셀로만 이동 (역방향 접근)
3. 각 바다에서 도달 가능한 셀들을 Set에 저장
4. 두 Set의 교집합으로 양쪽 바다 모두 도달 가능한 지점 반환
"""
# 원본 코드
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            visited.add((r, c))
            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if (new_r < 0 or new_r >= rows or
                    new_c < 0 or new_c >= cols or
                    (new_r, new_c) in visited):
                    continue
                if heights[new_r][new_c] >= heights[r][c]:
                    dfs(new_r, new_c, visited)

        for c in range(cols):
            dfs(0, c, pacific)
        for r in range(rows):
            dfs(r, 0, pacific)

        for c in range(cols):
            dfs(rows-1, c, atlantic)
        for r in range(rows):
            dfs(r, cols-1, atlantic)

        return list(pacific & atlantic)

# 개선된 코드
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        # 각 바다에서 도달 가능한 위치 저장
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            # 현재 위치 방문 처리
            visited.add((r, c))

            # 네 방향 탐색 (오른쪽, 위, 왼쪽, 아래)
            for dr, dc in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
                new_r, new_c = r + dr, c + dc

                # 경계 체크, 방문x 체크, 높이 체크
                if (0 <= new_r < rows and
                    0 <= new_c < cols and
                    (new_r, new_c) not in visited and
                    heights[new_r][new_c] >= heights[r][c]):

                    dfs(new_r, new_c, visited)

        # Pacific 경계에서 시작 (위 + 왼쪽)
        for c in range(cols):
            dfs(0, c, pacific)
        for r in range(rows):
            dfs(r, 0, pacific)

        # Atlantic 경계에서 시작 (아래 + 오른쪽)
        for c in range(cols):
            dfs(rows-1, c, atlantic)
        for r in range(rows):
            dfs(r, cols-1, atlantic)

        # 양쪽 바다 모두 도달 가능한 위치 반환
        return [[r, c] for r, c in pacific & atlantic]
