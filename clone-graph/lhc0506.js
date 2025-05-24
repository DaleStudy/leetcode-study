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
var cloneGraph = function(node) {
  if (!node) return null;

  const stack = [node];
  const map = new Map();

  map.set(node.val, new _Node(node.val));

  while (stack.length > 0) {
      const currentNode = stack.pop();

      for (const neighbor of currentNode.neighbors) {
          if (!map.has(neighbor.val)) {
              map.set(neighbor.val, new Node(neighbor.val));
              stack.push(neighbor);
          }
          map.get(currentNode.val).neighbors.push(map.get(neighbor.val));
      }

  }
  return map.get(node.val);
};


// 시간복잡도: O(n)
// 공간복잡도: O(n)
