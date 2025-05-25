/**
 * https://leetcode.com/problems/clone-graph/
 * // Definition for a _Node.
 * function _Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 * 시간 복잡도: O(N) — 노드 수만큼 순회
 * 공간 복잡도: O(N) — visited 맵과 재귀 호출 스택
 */

/**
 * @param {_Node} node
 * @return {_Node}
 */
var cloneGraph = function (node) {
  if (!node) return null;

  const visited = new Map();

  const dfs = (n) => {
    if (visited.has(n)) {
      return visited.get(n);
    }

    const clone = new Node(n.val);
    visited.set(n, clone);

    for (let neighbor of n.neighbors) {
      clone.neighbors.push(dfs(neighbor));
    }

    return clone;
  };

  return dfs(node);
};
