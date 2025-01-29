/**
 * // Definition for a _Node.
 * function _Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {_Node} node
 * @return {_Node}
 */

// BFS approach
// Time Complexity: O(N + E), where N is the number of nodes and E is the number of edges.
// Space Complexity: O(N), due to the clones map and additional storage (queue for BFS, recursion stack for DFS).

var cloneGraph = function (node) {
  if (!node) {
    return null;
  }
  let clone = new Node(node.val);
  let clones = new Map();
  clones.set(node, clone);
  let queue = [node];
  while (queue.length > 0) {
    node = queue.shift();
    for (const neighbor of node.neighbors) {
      if (!clones.get(neighbor)) {
        const temp = new Node(neighbor.val);
        clones.set(neighbor, temp);
        queue.push(neighbor);
      }
      clones.get(node).neighbors.push(clones.get(neighbor));
    }
  }

  return clone;
};

// DFS approach
// Time Complexity: O(N + E), where N is the number of nodes and E is the number of edges.
// Space Complexity: O(N), due to the clones map and the recursion stack.

var cloneGraph = function (node) {
  if (!node) {
    return null;
  }

  let clones = new Map();

  const dfs = (node) => {
    if (clones.has(node)) {
      return clones.get(node);
    }
    let clone = new Node(node.val);
    clones.set(node, clone);

    for (neighbor of node.neighbors) {
      clone.neighbors.push(dfs(neighbor));
    }

    return clone;
  };

  return dfs(node);
};

