"""
Valid Tree의 조건:
1. 모든 노드가 연결되어 있어야 함
2. 사이클이 없어야 함 
3. edge의 개수는 n-1개

Time Complexity: O(V + E)  
- V: 노드의 개수
- E: edge의 개수

Space Complexity: O(V)
- 노드 방문 여부를 저장하는 visited set 사용

풀이방법:
1. 기본 조건 체크: edge의 개수는 n-1개
2. 각 노드별로 연결된 노드들의 정보를 저장
   - 무방향 그래프이므로 양쪽 모두 저장
3. DFS로 노드 탐색
   - 0번 노드부터 시작해서 연결된 모든 노드를 방문
   - 이미 방문한 노드는 재방문하지 않음
4. 모든 노드 방문 확인
   - visited의 크기가 n과 같다면 모든 노드가 연결된 것 -> valid tree
"""
def validTree(n, edges):
    if len(edges) != n - 1:
        return False
    
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    
    visited = set()
    
    def dfs(node):
        if node in visited:
            return
        
        visited.add(node)
        
        for next_node in adj[node]:
            dfs(next_node)
    
    dfs(0)
    return len(visited) == n

