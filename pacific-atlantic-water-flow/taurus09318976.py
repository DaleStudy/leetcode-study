'''
문제의 핵심 포인트: 
물은 현재 높이보다 낮거나 같은 인접 셀로만 흐를 수 있음
즉, heights[현재] ≥ heights[인접]일 때 물이 흐름
태평양이 왼쪽, 위쪽 경계
대서양이 오른쪽, 아래쪽 경계

해결방법 :
역방향 접근법을 사용함. 즉, 바다에서 거꾸로 추적해서 어떤 셀들이 그 바다에 물을 보낼 수 있는지 찾는 방식임. 
이 방식이 각 셀을 개별적으로 확인할 필요가 없고, 시간 복잡도가 O(mxn)으로 최적화 되어 더 효율적임.
1. 태평양에서 시작해서 역류할 수 있는 모든 셀 찾기
2. 대서양에서 시작해서 역류할 수 있는 모든 셀 찾기
3. 두 바다 모두에서 도달 가능한 셀들의 교집합 구하기


시간 복잡도: O(m × n)
각 셀을 최대 한 번씩만 방문하므로 O(m × n)
DFS는 각 셀에서 최대 한 번만 실행됨 (집합을 통한 중복 방문 방지)

공간 복잡도: O(m × n)
pacific_reachable과 atlantic_reachable 집합이 각각 최대 m × n개의 좌표 저장
DFS 재귀 호출 스택의 최대 깊이도 O(m × n)

'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 격자의 크기를 구함
        m, n = len(heights), len(heights[0])
        
        # 각 바다에서 도달 가능한 셀들을 저장할 집합 생성
        pacific_reachable = set()
        atlantic_reachable = set()
        
        # DFS 함수 정의 : 현재 위치(r,c),도달 가능한 집합, 이전 셀의 높이를 매개변수로 받음
        def dfs(r, c, reachable, prev_height):
            # 경계를 벗어나거나 이미 방문했거나, 현재 높이가 이전 높이보다 낮으면 탐색 종료
            if (r < 0 or r >= m or c < 0 or c >= n or 
                (r, c) in reachable or heights[r][c] < prev_height):
                return
            
            # 현재 셀을 도달 가능한 집합에 추가
            reachable.add((r, c))
            
            # 4방향으로 재귀적으로 DFS 탐색
            dfs(r + 1, c, reachable, heights[r][c])  # 아래
            dfs(r - 1, c, reachable, heights[r][c])  # 위
            dfs(r, c + 1, reachable, heights[r][c])  # 오른쪽
            dfs(r, c - 1, reachable, heights[r][c])  # 왼쪽
        
        # 태평양 경계(위쪽, 왼쪽 경계)에서 시작하여 역류 가능한 모든 셀 탐색
        for i in range(m):
            dfs(i, 0, pacific_reachable, 0)         # 왼쪽 경계
        for j in range(n):
            dfs(0, j, pacific_reachable, 0)         # 위쪽 경계
        
        # 대서양 경계에서 DFS 시작 (아래쪽, 오른쪽 경계)
        for i in range(m):
            dfs(i, n - 1, atlantic_reachable, 0)    # 오른쪽 경계
        for j in range(n):
            dfs(m - 1, j, atlantic_reachable, 0)    # 아래쪽 경계
        
        # 두 바다 모두에서 도달 가능한 셀들의 교집합 구해서 결과 리스트에 추가
        result = []
        for r, c in pacific_reachable & atlantic_reachable:
            result.append([r, c])
        
        return result


       
