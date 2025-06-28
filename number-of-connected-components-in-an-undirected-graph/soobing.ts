/**
 * 문제 설명
 * - 무방향 그래프에서 연결된 노드의 갯수를 구하는 문제
 *
 * 아이디어
 * 1) 그래프 생성 + DFS로 탐색
 * 2) Union-Find -> ⚠️ 다음에 이걸로 해보기
 *   - 모든 노드를 자기 자신을 부모로 초기화
 *   - 각 edge에 대해 union 연산 수행
 *   - 최종적으로 남아있는 루트(대표 노드)의 개수가 연결 요소 수
 */
function countComponents(n: number, edges: number[][]): number {
  const graph: Record<number, number[]> = {};
  for (let i = 0; i < n; i++) graph[i] = [];

  for (const [a, b] of edges) {
    graph[a].push(b);
    graph[b].push(a);
  }

  const visited = new Set<number>();
  let count = 0;

  const dfs = (node: number) => {
    visited.add(node);
    for (const neighbor of graph[node]) {
      if (!visited.has(neighbor)) {
        dfs(neighbor);
      }
    }
  };

  for (let i = 0; i < n; i++) {
    if (!visited.has(i)) {
      dfs(i);
      count++;
    }
  }

  return count;
}

function countComponents2(n: number, edges: number[][]): number {
  const parent = Array(n)
    .fill(0)
    .map((_, i) => i);

  // find 함수 (경로 압축 포함)
  const find = (x: number): number => {
    if (parent[x] !== x) {
      parent[x] = find(parent[x]);
    }
    return parent[x];
  };

  // union 함수 (다른 집합이면 병합하고 true 반환)
  const union = (x: number, y: number): boolean => {
    const rootX = find(x);
    const rootY = find(y);
    if (rootX === rootY) return false;
    parent[rootX] = rootY;
    return true;
  };

  let count = n;

  for (const [a, b] of edges) {
    if (union(a, b)) {
      count--; // 서로 다른 집합을 연결했으므로 연결 요소 수 줄임
    }
  }

  return count;
}
