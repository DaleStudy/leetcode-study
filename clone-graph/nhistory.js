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
var cloneGraph = function (node) {
  let visited = {};

  const dfs = (node) => {
    if (!node) return node;
    if (visited[node.val]) return visited[node.val];

    let root = new Node(node.val);
    visited[node.val] = root;

    for (let neighbor of node.neighbors) {
      root.neighbors.push(dfs(neighbor));
    }
    return root;
  };

  return dfs(node);
};

// TC: O(n+e) -> n: number of nodes | e: number of edges
// SC: O(v) -> v: length of visited object
