"""
Constraints:
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- All the pairs prerequisites[i] are unique.

Time Complexity: O(N + P) 
- N: numCourses, P: prerequisites의 길이

Space Complexity: O(N + P) 
- 세트의 메모리 사용량이 N과 비례하고 인접 리스트의 크기가 P
- 재귀 호출 스택의 깊이는 최악의 경우 O(N)

풀이방법:
1. prerequisites을 directed graph로 변환
  - 각 코스별로 선수과목의 리스트를 저장함
2. DFS를 사용하여 cycle 존재 여부 확인
  - visited 배열: 이미 확인이 완료된 노드 체크
  - path 배열: 현재 DFS 경로에서 방문한 노드 체크
3. cycle이 발견되면 false, 그렇지 않으면 true 반환
  - 현재 경로에서 이미 방문한 노드를 다시 만나면 cycle 있음
  - 모든 노드 방문이 가능하면 cycle 없음
"""
class Solution:
   def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
       graph = [[] for _ in range(numCourses)]
       for course, prereq in prerequisites:
           graph[course].append(prereq)
       
       visited = [False] * numCourses
       path = [False] * numCourses
       
       def dfs(course):
           if path[course]:
               return False
           if visited[course]:
               return True
               
           path[course] = True
           
           for prereq in graph[course]:
               if not dfs(prereq):
                   return False
                   
           path[course] = False
           visited[course] = True
           
           return True
       
       for course in range(numCourses):
           if not dfs(course):
               return False
       
       return True

