export class Solution {
  /**
   * @param n: the number of vertices
   * @param edges: the edges of undirected graph
   * @return: the number of connected components
   */
  countComponents(n, edges) {
    // write your code here
    const graph = Array.from({ length: n }, () => []);

    for (const [node, neighbor] of edges) {
      graph[node].push(neighbor);
      graph[neighbor].push(node);
    }

    let visited = new Set();
    let count = 0;

    const dfs = (node) => {
      visited.add(node);
      for (const nei of graph[node]) {
        if (!visited.has(nei)) dfs(nei);
      }
    };

    for (let node = 0; node < n; node++) {
      if (!visited.has(node)) {
        count++;
        dfs(node);
      }
    }
    return count;
  }
}

// n: number of node | e: number of edge
// TC: O(n+e)
// SC: O(n+e)
