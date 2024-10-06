/**
 * TC: O(V + E)
 * 모든 정점를 방문하게 되고
 * 방문한 정점에서 연결된 간선을 queue에 추가하는 반복문을 실행합니다.
 * 따라서 시간복잡도는 정점 + 간선에 선형적으로 비례합니다.
 *
 * SC: O(V + E)
 * memory, visitedNodeVal 에서 V만큼 데이터 공간을 가집니다.
 * 그리고 queue에서 최대 모든 간선 갯수 * 2 만큼 갖게 됩니다.
 * 따라서 O(V + 2E) = O(V + E)로 계산했습니다.
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
