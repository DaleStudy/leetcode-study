/**
 * https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph
 * T.C. O(V + E)
 * S.C. O(V + E)
 */
function countComponents(n: number, edges: number[][]): number {
  const graph = new Map<number, number[]>();

  for (let i = 0; i < n; i++) {
    graph.set(i, []);
  }

  for (const [u, v] of edges) {
    graph.get(u)!.push(v);
    graph.get(v)!.push(u);
  }

  function dfs(node: number) {
    visited.add(node);

    for (const neighbor of graph.get(node)!) {
      if (!visited.has(neighbor)) {
        dfs(neighbor);
      }
    }
  }

  const visited = new Set<number>();

  let components = 0;

  for (let i = 0; i < n; i++) {
    if (!visited.has(i)) {
      components++;
      dfs(i);
    }
  }

  return components;
}

/**
 * Using Union Find
 * T.C. O(V + E)
 *
 */
function countComponents(n: number, edges: number[][]): number {
  const parent = Array.from({ length: n }, (_, i) => i);

  // find and compress path
  function find(x: number): number {
    if (parent[x] !== x) {
      parent[x] = find(parent[x]);
    }
    return parent[x];
  }

  // union two sets and check if they have the same root
  function union(x: number, y: number): boolean {
    const rootX = find(x);
    const rootY = find(y);
    parent[rootX] = rootY;
    return true;
  }

  for (const [x, y] of edges) {
    union(x, y);
  }

  return new Set(parent.map(find)).size;
}
