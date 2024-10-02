/**
 * https://leetcode.com/problems/clone-graph
 * T.C. O(N)
 * S.C. O(N)
 */
function cloneGraph(node: _Node | null): _Node | null {
  if (!node) return null;

  const map = new Map<number, _Node>();
  return dfs(node);

  function dfs(node: _Node): _Node {
    if (map.has(node.val)) return map.get(node.val)!;

    const newNode = new _Node(node.val);
    map.set(node.val, newNode);

    for (let neighbor of node.neighbors) {
      newNode.neighbors.push(dfs(neighbor));
    }

    return newNode;
  }
}

/**
 * T.C. O(N)
 * S.C. O(N)
 */
function cloneGraph(node: _Node | null): _Node | null {
  if (!node) return null;

  const map = new Map<number, _Node>();
  const stack = [node];
  const newNode = new _Node(node.val);
  map.set(node.val, newNode);

  while (stack.length) {
    const node = stack.pop()!;
    const newNode = map.get(node.val)!;

    for (let neighbor of node.neighbors) {
      if (!map.has(neighbor.val)) {
        stack.push(neighbor);
        const newNeighbor = new _Node(neighbor.val);
        map.set(neighbor.val, newNeighbor);
      }
      newNode.neighbors.push(map.get(neighbor.val)!);
    }
  }

  return newNode;
}

class _Node {
  val: number;
  neighbors: _Node[];

  constructor(val?: number, neighbors?: _Node[]) {
    this.val = val === undefined ? 0 : val;
    this.neighbors = neighbors === undefined ? [] : neighbors;
  }
}
