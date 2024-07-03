// Time Complexity: O(n)
// Space Complexity: O(n)

class Solution {
  validTree(n, edges) {
    // initialize Union-Find data structure
    const parent = Array(n)
      .fill(0)
      .map((_, index) => index);
    const rank = Array(n).fill(1);

    // find function with path compression
    function find(x) {
      if (parent[x] !== x) {
        parent[x] = find(parent[x]);
      }
      return parent[x];
    }

    // union function with union by rank
    function union(x, y) {
      const rootX = find(x);
      const rootY = find(y);
      if (rootX !== rootY) {
        if (rank[rootX] > rank[rootY]) {
          parent[rootY] = rootX;
        } else if (rank[rootX] < rank[rootY]) {
          parent[rootX] = rootY;
        } else {
          parent[rootY] = rootX;
          rank[rootX] += 1;
        }
      } else {
        // if rootX == rootY, there is a cycle
        return false;
      }
      return true;
    }

    // process each edge
    for (const [u, v] of edges) {
      if (!union(u, v)) {
        // if union returns false, a cycle is detected
        return false;
      }
    }

    // if all unions are successful, it's a valid tree
    return true;
  }
}
