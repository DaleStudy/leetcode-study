/**
 * Definition for _Node.
 * class _Node {
 *     val: number
 *     neighbors: _Node[]
 *
 *     constructor(val?: number, neighbors?: _Node[]) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.neighbors = (neighbors===undefined ? [] : neighbors)
 *     }
 * }
 *
 */

function cloneGraph(node: _Node | null): _Node | null {
  if (!node) return null;

  const cloned = new Map<number, _Node>();

  const queue: _Node[] = [];

  const copied = new _Node(node.val);
  cloned.set(node.val, copied);

  queue.push(node);

  let pointer = 0;

  while (pointer < queue.length) {
    const current = queue[pointer++];

    const copiedNode = cloned.get(current.val)!;

    for (const neighbor of current.neighbors) {
      if (!cloned.has(neighbor.val)) {
        const copiedNeighbor = new _Node(neighbor.val);
        cloned.set(neighbor.val, copiedNeighbor);

        queue.push(neighbor);
      }
      copiedNode.neighbors.push(cloned.get(neighbor.val)!);
    }
  }

  return copied;
}
