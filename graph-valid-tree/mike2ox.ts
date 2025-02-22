/**
 * Source: https://www.lintcode.com/problem/178/
 * Solution: 유효한 트리인지 순회하면서 확인하면 되기에 BFS로 구현
 * 시간 복잡도: O(V + E) - 노드와 간선에 한번은 방문
 * 공간 복잡도: O(V + E) - 인접리스트 만큼의 공간 필요
 */
function validTree(n: number, edges: number[][]): boolean {
  // 간선 개수 체크: 트리는 노드 개수 - 1개의 간선을 가져야 함
  if (edges.length !== n - 1) return false;

  // 인접 리스트
  const adjList: Map<number, number[]> = new Map();
  for (let i = 0; i < n; i++) {
    adjList.set(i, []);
  }

  // 양방향 그래프 구성
  for (const [u, v] of edges) {
    adjList.get(u)!.push(v);
    adjList.get(v)!.push(u);
  }

  const queue: [number, number][] = [[0, -1]]; // [노드, 부모노드]
  const visited: Set<number> = new Set([0]);

  while (queue.length > 0) {
    const [node, parent] = queue.shift()!;

    // 모든 이웃 노드 확인
    for (const neighbor of adjList.get(node)!) {
      // 부모 노드는 continue
      if (neighbor === parent) continue;

      // 이미 방문한 노드를 만나면 사이클 존재
      if (visited.has(neighbor)) return false;

      // 이웃 노드를 큐에 추가하고 방문 표시
      visited.add(neighbor);
      queue.push([neighbor, node]);
    }
  }

  // 모든 노드가 연결되어 있는지 확인
  return visited.size === n;
}
