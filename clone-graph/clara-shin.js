/**
 * BFS를 사용한 그래프 복제
 * @param {_Node} node
 * @return {_Node}
 */
var cloneGraph = function (node) {
  if (!node) return null;

  // 원본 노드와 복제된 노드를 매핑하는 해시맵
  const cloned = new Map();

  // BFS를 위한 큐
  const queue = [node];

  // 시작 노드 복제
  cloned.set(node, new _Node(node.val));

  while (queue.length > 0) {
    const currentNode = queue.shift();

    // 현재 노드의 모든 이웃들을 처리
    for (let neighbor of currentNode.neighbors) {
      // 이웃이 아직 복제되지 않았다면
      if (!cloned.has(neighbor)) {
        // 새로운 노드 생성하고 맵에 저장
        cloned.set(neighbor, new _Node(neighbor.val));
        // 큐에 추가하여 나중에 처리
        queue.push(neighbor);
      }

      // 복제된 현재 노드의 이웃 리스트에 복제된 이웃 추가
      cloned.get(currentNode).neighbors.push(cloned.get(neighbor));
    }
  }

  return cloned.get(node);
};
