// v: len(vertexes), e: len(edges)
// Time complexity: O(v + e)
// Space complexity: O(v + e)

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
  const nodes = Array.from({ length: 101 }, (_, i) => null);

  const dfs = (node) => {
    if (!node) {
      return;
    }

    if (nodes[node.val]) {
      return nodes[node.val];
    }

    const newNode = new _Node(node.val);
    nodes[node.val] = newNode;

    for (const neighbor of node.neighbors) {
      const cloned = dfs(neighbor);
      newNode.neighbors.push(cloned);
    }

    return newNode;
  };

  dfs(node);

  return nodes[1];
};
