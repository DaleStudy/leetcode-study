class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. 그래프 만들기 (인접 리스트)
        # graph[A] = [B, C] : A를 듣기 위해 B, C가 필요함 (혹은 방향에 따라 반대)
        graph = collections.defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        # 2. 방문 상태 기록 (0, 1, 2)
        # 0: 아직 안 가봄 (White)
        # 1: 지금 탐색 중인 경로 (Grey) -> 여기서 또 만나면 뱅글뱅글 도는 것(사이클)!
        # 2: 이미 검증 끝남 (Black) -> 안전함
        visit = [0] * numCourses

        def dfs(course):
            # 탐색 중인 노드를 다시 만남 == 사이클 발생!
            if visit[course] == 1:
                return False
            
            # 이미 검증 끝난 노드 == 문제 없음 Pass
            if visit[course] == 2:
                return True
            
            # 현재 노드를 '탐색 중(1)'으로 표시
            visit[course] = 1
            
            # 선수 과목들 쭉 파고들기
            for pre in graph[course]:
                if not dfs(pre):  # 재귀 호출 결과가 False(사이클 발견)라면
                    return False  # 즉시 False 리턴
            
            # 더 이상 갈 곳 없음. '탐색 완료(2)'로 표시
            visit[course] = 2
            return True

        # 3. 모든 과목에 대해 확인 (그래프가 여러 덩어리일 수 있으므로)
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
