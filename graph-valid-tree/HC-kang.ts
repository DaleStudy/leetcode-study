/**
 * https://leetcode.com/problems/graph-valid-tree
 * T.C. O(n)
 * S.C. O(n)
 */
function validTree(n: number, edges: number[][]): boolean {
  if (edges.length !== n - 1) return false;

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
    if (rootX === rootY) return false;
    parent[rootX] = rootY;
    return true;
  }

  for (const [x, y] of edges) {
    if (!union(x, y)) return false;
  }

  return true;
}
