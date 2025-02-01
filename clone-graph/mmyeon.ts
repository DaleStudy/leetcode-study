class _Node {
  val: number;
  neighbors: _Node[];
  constructor(val?: number, neighbors?: _Node[]) {
    this.val = val === undefined ? 0 : val;
    this.neighbors = neighbors === undefined ? [] : neighbors;
  }
}

/**
 * @link https://leetcode.com/problems/clone-graph/description/
 *
 * 접근 방법 :
 *  - 엣지 케이스 : 주어진 노드가 null이면 그대로 리턴
 *  - 이미 방문한 노드인지 확인 : 방문한 노드인 경우, 저장된 복사 노드 리턴해서 중복 생성 방지
 *  - 새로운 노드 클론하고 visited 맵에 저장
 *  - 해당 노드의 이웃 노드도 순회하면서 복제
 *  - 클론된 노드 리턴
 *
 * 시간복잡도 : O(n + e)
 *  - n은 노드의 개수, e는 노드 연결하는 엣지의 개수
 *  - 모든 노드 순회하면서 각 노드의 이웃 탐색
 *
 * 공간복잡도 : O(n)
 *  - 모든 노드를 클론해서 visited 맵에 저장되므로 O(n)
 *  - 그래프가 선형 구조인 최악의 경우, 재귀 호출 스택이 O(n)
 */
function cloneGraph(node: _Node | null): _Node | null {
  if (!node) return null;
  const visited = new Map<number, _Node>();

  const cloneNode = (node: _Node): _Node => {
    if (visited.has(node.val)) return visited.get(node.val) as _Node;

    const clonedNode = new _Node(node.val);
    visited.set(node.val, clonedNode);

    for (const neighbor of node.neighbors) {
      const clonedNeighbor = cloneNode(neighbor);

      clonedNode.neighbors.push(clonedNeighbor);
    }

    return clonedNode;
  };

  return cloneNode(node);
}
