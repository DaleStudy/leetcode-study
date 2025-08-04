// Time Complexity: O(n + e) — 노드 n개와 간선 e개를 한 번씩 순회
// Space Complexity: O(n + e) — 인접 리스트 저장 O(n+e), 재귀 호출 스택 최악 O(n)
function countComponents(n, edges) {
  // 인접 리스트 생성
  const adj = Array.from({ length: n }, () => []);
  for (const [u, v] of edges) {
    adj[u].push(v);
    adj[v].push(u);
  }

  const visited = Array(n).fill(false);
  let count = 0;

  function dfs(u) {
    visited[u] = true;
    for (const v of adj[u]) {
      if (!visited[v]) dfs(v);
    }
  }

  // 모든 노드 순회
  for (let i = 0; i < n; i++) {
    if (!visited[i]) {
      count++;
      dfs(i);
    }
  }

  return count;
}
