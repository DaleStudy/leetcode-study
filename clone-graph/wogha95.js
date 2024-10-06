/**
 * TC: O(E)
 * graph에 연결된 edge만큼 queue에 추가, 제거하며 순회한다.
 *
 * SC: O(V + E)
 * cloned graph만큼 공간 복잡도 생성해야한다.
 *
 * V: vertex, E: edge
 */

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
  if (!node) {
    return null;
  }

  const memory = new Map();
  const visitedNodeVal = new Set();

  return bfsClone(node);

  // 1. bfs로 순회하면서 deep clone한 graph의 head를 반환
  function bfsClone(start) {
    const queue = [start];
    const clonedHeadNode = new _Node(start.val);
    memory.set(start.val, clonedHeadNode);

    while (queue.length > 0) {
      const current = queue.shift();
      if (visitedNodeVal.has(current.val)) {
        continue;
      }

      const clonedCurrentNode = getCloneNode(current.val);

      for (const neighbor of current.neighbors) {
        const clonedNeighborNode = getCloneNode(neighbor.val);
        clonedCurrentNode.neighbors.push(clonedNeighborNode);

        queue.push(neighbor);
      }

      visitedNodeVal.add(current.val);
    }

    return clonedHeadNode;
  }

  // 2. memory에 val에 해당하는 node 반환 (없을 경우 생성)
  function getCloneNode(val) {
    if (!memory.has(val)) {
      const node = new _Node(val);
      memory.set(val, node);
      return node;
    }

    return memory.get(val);
  }
};
