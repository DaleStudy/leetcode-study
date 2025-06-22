export class Solution {
  /**
   * @param {number} n - the number of vertices
   * @param {number[][]} edges - the edges of undirected graph
   * @return {number} - the number of connected components
   */
  countComponents(n, edges) {
    const par = Array.from({ length: n }, (_, i) => i);
    const rank = Array(n).fill(1);

    const find = (n1) => {
      let res = n1;
      while (res !== par[res]) {
        par[res] = par[par[res]]; // path compression
        res = par[res];
      }
      return res;
    };

    const union = (n1, n2) => {
      const p1 = find(n1);
      const p2 = find(n2);
      if (p1 === p2) return 0;

      if (rank[p2] > rank[p1]) {
        par[p1] = p2;
        rank[p2] += rank[p1];
      } else {
        par[p2] = p1;
        rank[p1] += rank[p2];
      }

      return 1;
    };

    let res = n;
    for (const [n1, n2] of edges) {
      res -= union(n1, n2);
    }

    return res;
  }
}

