'''
# 323. Number of Connected Components in an Undirected Graph

- 무방향 그래프에서 연결된 컴포넌트(connected component)의 개수 구하기
- 노드 개수 n: 0 ~ n-1
- 간선 리스트 edges: 노드 쌍 [u, v]
- 연결된 컴포넌트의 개수를 반환한다.

## 그래프
- edges를 통해 인접 리스트(adjacency list)를 생성한다.
- 무방향 그래프이므로, u ↔ v 양쪽 방향으로 연결

## 풀이 알고리즘
- DFS(스택)/BFS(큐)
  - 각 컴포넌트를 탐색하며 방문 처리
  - 방문하지 않은 노드를 찾으면 새로운 컴포넌트이므로 카운트 증가
- Union-Find
  - 각 노드가 어떤 그룹에 속하는 지 parent 배열로 표현
  - find로 부모를 찾고, union으로 노드를 합친다.
  - 최종적으로 독립된 그룹의 개수를 반환한다.
'''

'''
1. DFS(스택)
'''
def countComponentsDFS(self, n: int, edges: List[List[int]]) -> int:
  graph = defaultdict(list)
  for u, v in edges: # 인접 리스트 생성
    graph[u].append(v)
    graph[v].append(u)
  
  visited = set() # 방문처리할 set
  count = 0
  
  def dfs(start):
    stack = [start]
    visited.add(start)

    while stack:
      curr = stack.pop()
      for neighbor in graph[curr]:
        if neighbor not in visited:
          visited.add(neighbor)
          stack.append(neighbor)
          
  for node in range(n):
    if node not in visited:
      dfs(node)
      count += 1
  
  return count

'''
2. BFS(큐)
'''
def countComponentsBFS(self, n: int, edges: List[List[int]]) -> int:
  graph = defaultdict(list)
  for u, v in edges: # 인접 리스트 생성
    graph[u].append(v)
    graph[v].append(u)
  
  visited = set() # 방문처리할 set
  count = 0
  
  def bfs(start):
    queue = deque([start])
    visited.add(start)

    while queue:
      curr = queue.popleft()
      for neighbor in graph[curr]:
        if neighbor not in visited:
          visited.add(neighbor)
          queue.append(neighbor)
        
  for node in range(n):
    if node not in visited:
      bfs(node)
      count += 1
  
  return count

'''
3. Union-Find
- 간선을 순회하며 두 노드를 union으로 합친다.(parent 업데이트)
- find는 경로 압축을 통해 대표(root)를 찾는다.(parent에서 재귀로 찾기)
- 최종 root를 조사하고, 서로 다른 root의 개수를 반환한다.
'''
def countComponentsUnionFind(self, n: int, edges: List[List[int]]) -> int:
  parent = list(range(n)) # 각 노드의 부모를 자신으로 초기화

  def find(x):
    if parent[x] != x:
      parent[x] = find(parent[x]) # 경로 압축 path compression
    return parent[x]
  
  def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
      parent[rootX] = rootY
  
  for u, v in edges:
    union(u, v)
  
  # 모든 노드의 최종 부모의, 유일한 root의 개수를 반환
  return len(set(find(i) for i in range(n)))
