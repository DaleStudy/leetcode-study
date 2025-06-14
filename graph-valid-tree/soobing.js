/**
 * 문제 설명
 * - 주어진 간선 정보로 트리가 만들어지는지 확인하는 문제
 * - 어려웠음 다시 풀어보기 ⚠️
 * 
 * 트리의 조건
 * 1) 모든 노드가 연결되어 있어야 한다.
 * 2) 사이클이 없어야 한다.
 * 3) 총 간선의 갯수는 n-1개여야 한다.
 * 
 * 아이디어
 * 1) Union-Find (Disjoint Set)
 * 2) DFS ✅
 */
function validTree(n, edges) {
  if (edges.length !== n - 1) return false; // 간선 수가 n - 1이 아니면 트리 불가

  const graph = Array.from({ length: n }, () => []);
  for (const [a, b] of edges) {
    graph[a].push(b);
    graph[b].push(a);
  }

  const visited = new Set();

  const dfs = (node, prev) => {
    if (visited.has(node)) return false;
    visited.add(node);

    for (const neighbor of graph[node]) {
      if (neighbor === prev) continue; // 바로 이전 노드는 무시, 체크하는 이유: 무방향 그래프이기 때문에 사이클로 들어가게 하지 않기 위함.
      if (!dfs(neighbor, node)) return false; // 사이클 발생
    }

    return true;
  };

  if (!dfs(0, -1)) return false;

  return visited.size === n;
}
