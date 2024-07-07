// Time Complexity: O(n + m) m : number of edges
// Space Complexity: O(n)

class Solution {
  countComponents(n, edges) {
    // initialize the parent array where each node is its own parent initially
    const parent = new Array(n).fill(0).map((_, index) => index);

    // to find the root of a node with path compression
    const find = (node) => {
      if (parent[node] !== node) {
        parent[node] = find(parent[node]);
      }
      return parent[node];
    };

    // to union two nodes
    const union = (node1, node2) => {
      const root1 = find(node1);
      const root2 = find(node2);
      if (root1 !== root2) {
        parent[root1] = root2;
      }
    };

    // union all the edges
    for (let [a, b] of edges) {
      union(a, b);
    }

    // count the number of unique roots
    const uniqueRoots = new Set();
    for (let i = 0; i < n; i++) {
      uniqueRoots.add(find(i));
    }

    return uniqueRoots.size;
  }
}
