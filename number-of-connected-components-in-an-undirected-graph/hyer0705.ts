export class Solution {
  /**
   * @param n: the number of vertices
   * @param edges: the edges of undirected graph
   * @return: the number of connected components
   */
  countComponents(n: number, edges: number[][]): number {
    const parent = Array.from({ length: n }, (_, i) => i);
    let components = n;

    const find = (i: number): number => {
      if (parent[i] === i) {
        return i;
      }

      parent[i] = find(parent[i]);
      return parent[i];
    };

    const union = (a: number, b: number): void => {
      const rootA = find(a);
      const rootB = find(b);

      if (rootA !== rootB) {
        parent[rootA] = rootB;
        components--;
      }
    };

    for (const [a, b] of edges) {
      union(a, b);
    }

    return components;
  }
}
