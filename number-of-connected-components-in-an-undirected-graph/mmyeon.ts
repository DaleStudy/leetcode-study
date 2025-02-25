/**
 *@link https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph
 *
 * 접근 방법 : DFS 사용
 *  - 그래프를 인접 리스트로 저장
 *  - DFS 사용해서 연결된 모든 노드 방문 처리
 *  -방문하지 않은 노드 발견 시 count 증가
 *
 * 시간복잡도 : O(n + e)
 *  - n = 노드 개수, e = 엣지 개수
 *  - 모든 노드 순회해서 dfs 실행 : O(n)
 *  - edges 순회해서 graph 생성 : O(e)
 *
 * 공간복잡도 : O(n + e)
 *  - 노드와 인접된 리스트 저장 : O(n + e)
 */

function countComponents(n: number, edges: number[][]): number {
  const graph = new Map<number, number[]>();

  for (let i = 0; i < n; i++) {
    graph.set(i, []);
  }

  for (const [node1, node2] of edges) {
    graph.get(node1)!.push(node2);
    graph.get(node2)!.push(node1);
  }

  const visited: boolean[] = Array(n).fill(false);

  function dfs(node: number) {
    // 방문한 노드 처리
    visited[node] = true;
    for (const neighbor of graph.get(node) || []) {
      if (!visited[neighbor]) dfs(neighbor);
    }
  }

  let count = 0;
  for (let node = 0; node < n; node++) {
    // 처음 방문하는 노드인 경우
    if (!visited[node]) {
      count++;
      dfs(node);
    }
  }

  return count;
}
