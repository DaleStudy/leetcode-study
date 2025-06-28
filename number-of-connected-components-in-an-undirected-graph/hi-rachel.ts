/**
 * TC: O(N + E), N: 노드의 개수, E: 간선의 개수
 * SC: O(N + E)
 */

// DFS
function countComponentsDFS(n: number, edges: number[][]): number {
  const graph: number[][] = Array.from({ length: n }, () => []);

  // 그래프 초기화
  for (const [u, v] of edges) {
    graph[u].push(v);
    graph[v].push(u);
  }

  const visited = new Set<number>();

  function dfs(node: number) {
    visited.add(node);
    for (const neighbor of graph[node]) {
      if (!visited.has(neighbor)) {
        dfs(neighbor);
      }
    }
  }

  let components = 0;
  for (let i = 0; i < n; i++) {
    if (!visited.has(i)) {
      components++;
      dfs(i);
    }
  }

  return components;
}

// BFS
function countComponentsBFS(n: number, edges: number[][]): number {
  const graph: number[][] = Array.from({ length: n }, () => []);

  // 그래프 초기화
  for (const [u, v] of edges) {
    graph[u].push(v);
    graph[v].push(u);
  }

  const visited = new Set<number>();
  let components = 0;

  for (let i = 0; i < n; i++) {
    if (!visited.has(i)) {
      components++;
      const queue: number[] = [i];

      while (queue.length > 0) {
        const node = queue.shift();
        if (node === undefined) continue;
        if (visited.has(node)) continue;
        visited.add(node);

        for (const neighbor of graph[node]) {
          if (!visited.has(neighbor)) queue.push(neighbor);
        }
      }
    }
  }

  return components;
}
