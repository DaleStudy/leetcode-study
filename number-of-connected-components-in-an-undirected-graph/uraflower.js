
/**
 * @param n: the number of vertices
 * @param edges: the edges of undirected graph
 * @return: the number of connected components
 */
const countComponents = function (n, edges) {
  // graph 만들기
  const graph = Array.from({ length: n }).map(() => []);

  for (const [u, v] of edges) {
    graph[u].push(v);
    graph[v].push(u);
  }

  // 각 노드 순회하기
  let count = 0;
  const visited = new Set();

  for (let i = 0; i < n; i++) {
    if (visited.has(i)) {
      continue;
    }

    count += 1;

    // bfs
    const queue = [i];
    visited.add(i);

    while (queue.length) {
      const u = queue.shift();

      for (const v of graph[u]) {
        if (!visited.has(v)) {
          visited.add(v);
          queue.push(v);
        }
      }
    }
  }

  return count;
}

// 시간복잡도: O(E)
// 공간복잡도: O(V)
