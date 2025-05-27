/**
 * // Definition for a Node.
 * function Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {Node} node
 * @return {Node}
 */
var cloneGraph = function (node) {
  if (!node) return null;

  const visited = new Map();

  const dfs = (currNode) => {
    if (visited.has(currNode)) {
      return visited.get(currNode);
    }

    // 노드 복사
    const clone = new Node(currNode.val);
    visited.set(currNode, clone);

    // 이웃 노드들도 복사해서 연결
    for (let neighbor of currNode.neighbors) {
      clone.neighbors.push(dfs(neighbor));
    }

    return clone;
  };

  return dfs(node);
};
