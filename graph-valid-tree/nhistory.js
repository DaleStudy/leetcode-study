class Solution {
  /**
   * @param {number} n
   * @param {number[][]} edges
   * @returns {boolean}
   */
  validTree(n, edges) {
    // A valid tree must have exactly n - 1 edges
    if (edges.length !== n - 1) {
      return false;
    }

    // Initialize the adjacency list
    let graph = [];
    for (let i = 0; i < n; i++) {
      graph.push([]);
    }

    // Populate the adjacency list with edges
    for (let [node, neighbor] of edges) {
      graph[node].push(neighbor);
      graph[neighbor].push(node);
    }

    let visited = new Set();

    // Depth-First Search (DFS) to explore the graph
    function dfs(node) {
      visited.add(node);
      for (let neighbor of graph[node]) {
        if (!visited.has(neighbor)) {
          dfs(neighbor);
        }
      }
    }

    // Start DFS from node 0
    dfs(0);

    // Check if all nodes were visited
    return visited.size === n;
  }
}

// TC: O(n)
// SC: O(n)
